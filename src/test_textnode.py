import unittest

from textnode import TextNode,TextType, text_node_to_html_node,text_to_textnodes
from split_delimiter import split_nodes_delimiter, split_nodes_images,split_nodes_link

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('this is a text node', TextType.BOLD)
        node2 = TextNode('this is a text node', TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode('this is a text node', TextType.BOLD)
        node2 = TextNode('this is a text node', TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.to_html(), '<b>This is a bold node</b>')


    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(TextNode("This is text with a ", TextType.TEXT), new_nodes[0])
        self.assertEqual(TextNode("code block", TextType.CODE),new_nodes[1])
        self.assertEqual(TextNode(" word", TextType.TEXT),new_nodes[2])


    def test_split_nodes_link(self):
        node = TextNode("Hello [world](https://example.com) friend", TextType.TEXT)
        new_nodes = split_nodes_link([node])

        self.assertEqual(new_nodes[0],TextNode("Hello ", TextType.TEXT))
        self.assertEqual(new_nodes[1],TextNode("world", TextType.LINK,'https://example.com'))
        self.assertEqual(new_nodes[2],TextNode(" friend", TextType.TEXT))


    def test_text_to_text_nodes(self):
        text = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        result = text_to_textnodes(text)
        self.assertEqual(result[0],TextNode("This is ", TextType.TEXT))
        self.assertEqual(result[1],TextNode("text", TextType.BOLD))
        self.assertEqual(result[2],TextNode(" with an ", TextType.TEXT))
        self.assertEqual(result[3],TextNode("italic", TextType.ITALIC))
        self.assertEqual(result[4],TextNode(" word and a ", TextType.TEXT))
        self.assertEqual(result[5],TextNode("code block", TextType.CODE))
        self.assertEqual(result[6],TextNode(" and an ", TextType.TEXT))
        self.assertEqual(result[7],TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"))
        self.assertEqual(result[8],TextNode(" and a ", TextType.TEXT))
        self.assertEqual(result[9],TextNode("link", TextType.LINK, "https://boot.dev"))





if __name__ == '__main__':
    unittest.main()