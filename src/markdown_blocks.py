from curses.ascii import isdigit
from enum import Enum

from htmlnode import HTMLNode, ParentNode,LeafNode
from textnode import text_to_textnodes, text_node_to_html_node, TextNode, TextType


class BlockType(Enum):
    paragraph = 1
    heading = 2
    code = 3
    quote = 4
    unordered_list = 5
    ordered_list = 6


def markdown_to_blocks(markdown):
    split_markdown = markdown.split('\n\n')
    blocks = []
    for i in range(len(split_markdown)):
        split_markdown[i] = split_markdown[i].strip()
        if split_markdown[i] != '':
            blocks.append(split_markdown[i])

    return blocks



def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children_html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children_html_nodes.append(html_node)

    return children_html_nodes


def block_to_block_type(block):
        count = 0
        length_of_line = 0
        current_line=[]

        if block.startswith('#'):
            count = 0
            length_of_line = 0
            current_line = []

            while count < len(block) and block[count] == '#':
                count += 1

            if 1 <= count <= 6 and count < len(block) and block[count] == ' ':

                return BlockType.heading


        elif block.startswith('```') and block.endswith('```'):


            return BlockType.code

        elif block.startswith('>'):
            count = 0
            length_of_line = 0
            current_line = []



            for line in block.split('\n'):
                if line.startswith('>'):
                    count+=1
                length_of_line+=1


            if count == length_of_line:
                return BlockType.quote


        elif block.startswith('- '):
            count = 0
            length_of_line = 0
            current_line = []

            for line in block.split('\n'):
                if line.startswith('- '):
                    count+=1

                length_of_line+=1

            if count == length_of_line:
                return BlockType.unordered_list


        elif block.startswith('1. '):
            count = 0
            length_of_line = 0
            current_line = []
            for line in block.split('\n'):
                current_line.append(line)
                length_of_line+=1

            for idx, line in enumerate(current_line):
                if line.startswith(f'{idx + 1}. '):
                    count+=1


            if count == length_of_line:
                return BlockType.ordered_list



        return BlockType.paragraph

def block_to_html(block_type, block):
    if block_type == BlockType.paragraph:
            split_block = block.split('\n')
            strip_block =[]
            for curr_block in split_block:
                curr_block = curr_block.strip()
                if curr_block:
                    strip_block.append(curr_block)

            block = ' '.join(strip_block)

            children_nodes = text_to_children(block)
            html_node = ParentNode('p', children_nodes,None)
            return html_node

    elif block_type == BlockType.heading:
        heading_count = 0
        while block[heading_count] == '#':
            heading_count += 1

        if block[heading_count] == ' ':
            block = block[heading_count+1:]
            children_nodes = text_to_children(block)
            return ParentNode(f'h{heading_count}',children_nodes, None)

    elif block_type == BlockType.code:
        lines = block.split('\n')
        inner_lines = lines[1:-1]
        inner_text = "\n".join(inner_lines)
        text_node = TextNode(inner_text,TextType.TEXT,None)
        child_html_node = text_node_to_html_node(text_node)
        html_node = ParentNode('code',[child_html_node],None)
        pre_html_node = ParentNode('pre',[html_node],None)

        return pre_html_node

    elif block_type == BlockType.quote:
        new_block=[]
        cleaned_lines = []
        content=None
        lines = block.split('\n')
        for line in lines:
            line = line.strip()

            if line.startswith('>'):
                content = line[1:].lstrip()

            else:
                content=line

            if content:
                cleaned_lines.append(content)

        block = ' '.join(cleaned_lines)
        children_nodes = text_to_children(block)
        html_node = ParentNode('blockquote',children_nodes,None)

        return html_node




    elif block_type == BlockType.unordered_list:
        li_tag=[]
        split_block = block.split('\n')

        for curr_block in split_block:
            if curr_block.startswith('- '):
                current_list = curr_block[2:]
                children_nodes = text_to_children(current_list)
                html_node = ParentNode('li',children_nodes,None)
                li_tag.append(html_node)


        main_html_node = ParentNode('ul',li_tag,None)
        return main_html_node



    elif block_type == BlockType.ordered_list:
       li_tag=[]
       split_block = block.split('\n')
       current_list =[]

       for idx,curr_block in enumerate(split_block):
            if curr_block.startswith(f'{idx + 1}. '):
                start_index =curr_block.find('.')+2
                current_list = curr_block[start_index:]


                children_nodes = text_to_children(current_list)
                html_node = ParentNode('li',children_nodes,None)
                li_tag.append(html_node)

       main_html_node = ParentNode('ol',li_tag,None)
       return main_html_node



    raise ValueError(f'Unknown block type: {block_type}')







def markdown_to_html_node(markdown):
    split_markdown = markdown_to_blocks(markdown)
    html_nodes=[]
    for block in split_markdown:
        block_type = block_to_block_type(block)
        html_nodes.append(block_to_html(block_type, block))

    parent_node = ParentNode('div',html_nodes,None)
    return parent_node