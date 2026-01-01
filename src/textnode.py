from enum import Enum

from htmlnode import LeafNode



class TextType(Enum):
    TEXT='text'
    BOLD='bold'
    ITALIC='italic'
    CODE ='code'
    LINK = 'link'
    IMAGE = 'image'


def text_node_to_html_node(text_node):

    if text_node.text_type == TextType.TEXT:
       return LeafNode(None,text_node.text,None)

    elif text_node.text_type == TextType.BOLD:
        return LeafNode('b',text_node.text,None)

    elif text_node.text_type == TextType.ITALIC:
        return LeafNode('i',text_node.text,None)

    elif text_node.text_type == TextType.CODE:
        return LeafNode('code',text_node.text,None)

    elif text_node.text_type == TextType.LINK:
        return  LeafNode('a',text_node.text,{"href":text_node.url})

    elif text_node.text_type == TextType.IMAGE:
        return LeafNode('img','',{"src":text_node.url, "alt":text_node.text})


    else:
        raise Exception("unknown text type")



def text_to_textnodes(text):
    from split_delimiter import (split_nodes_delimiter,split_nodes_images,split_nodes_link)
    if text:
        print(text.split('**'))
        nodes = [TextNode(text,TextType.TEXT)]
        nodes =split_nodes_delimiter(nodes,'**',TextType.BOLD)
        nodes = split_nodes_delimiter(nodes,'_',TextType.ITALIC)
        nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
        nodes = split_nodes_images(nodes)
        nodes = split_nodes_link(nodes)

        return nodes

    return []













class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True

        return False

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'





# This is for testing only




