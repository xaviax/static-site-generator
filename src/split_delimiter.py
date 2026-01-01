import struct

from textnode import TextNode,TextType
from inline_markdown import extract_markdown_links,extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:

            new_nodes.append(node)

        elif node.text_type is TextType.TEXT:
            parts=[]
            parts=node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception('invalid markdown, no closing delimiter')



            for  index in range(len(parts)):
                if index % 2 == 0:
                    new_nodes.append(TextNode(parts[index],TextType.TEXT,node.url))



                else:
                    new_nodes.append(TextNode(parts[index],text_type,node.url))


    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        # Only process plain text nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        # If no links, just keep the node as-is
        if not links:
            new_nodes.append(node)
            continue

        current_text = node.text
        for link_text, link_url in links:
            pattern = f"[{link_text}]({link_url})"
            # split only once
            parts = current_text.split(pattern, 1)
            before = parts[0]
            after = parts[1] if len(parts) > 1 else ""

            if before:
                new_nodes.append(TextNode(before,TextType.TEXT,None))

            new_nodes.append(TextNode(link_text,TextType.LINK,link_url))
            current_text = after

            # 1) if before not empty, make a TEXT node and append
            # 2) make a LINK node for link_text + link_url and append
            # 3) set current_text = after and continue

        if current_text:
            new_nodes.append(TextNode(current_text,TextType.TEXT,None))


        # after the loop, if current_text not empty, append a final TEXT node

    return new_nodes


def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        # Only process plain text nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        # If no links, just keep the node as-is
        if not images:
            new_nodes.append(node)
            continue

        current_text = node.text
        for image, image_link in images:
            pattern = f"![{image}]({image_link})"
            # split only once
            parts = current_text.split(pattern, 1)
            before = parts[0]
            after = parts[1] if len(parts) > 1 else ""

            if before:
                new_nodes.append(TextNode(before,TextType.TEXT,None))

            new_nodes.append(TextNode(image,TextType.IMAGE,image_link))
            current_text = after

            # 1) if before not empty, make a TEXT node and append
            # 2) make a LINK node for link_text + link_url and append
            # 3) set current_text = after and continue

        if current_text:
            new_nodes.append(TextNode(current_text,TextType.TEXT,None))


        # after the loop, if current_text not empty, append a final TEXT node

    return new_nodes











