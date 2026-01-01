import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        htmlnode = HTMLNode('<p>', 'this is a paragraph',None,{
    "href": "https://www.google.com",
    "target": "_blank",})

        htmlnode2 = HTMLNode('<p>', 'this is a paragraph',None,{
    "href": "https://www.google.com",
    "target": "_blank",})

        self.assertEqual(htmlnode, htmlnode2)


    def test_not_eq(self):
        htmlnode = HTMLNode('<p>', 'this is a paragraph',None,None)
        htmlnode2 = HTMLNode('<p>', 'this is a paragraph',None,{"href": "https://www.google.com",
    "target": "_blank",})

        self.assertNotEqual(htmlnode, htmlnode2)


class ParentNodeTest(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )



