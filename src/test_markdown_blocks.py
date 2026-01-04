import unittest
from markdown_blocks import markdown_to_blocks,block_to_block_type,BlockType,markdown_to_html_node

class TestMarkdownToBlocks(unittest.TestCase):


    def test_one(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""



        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )





class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph_block(self):
        block = "This is a normal paragraph of text."
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_heading_block(self):
        block = "### My Heading"
        self.assertEqual(block_to_block_type(block), BlockType.heading)

    def test_code_block(self):
        block = "```py\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.code)

    def test_quote_block(self):
        block = "> first line\n> second line"
        self.assertEqual(block_to_block_type(block), BlockType.quote)

    def test_unordered_list_block(self):
        block = "- item one\n- item two\n- item three"
        self.assertEqual(block_to_block_type(block), BlockType.unordered_list)

    def test_ordered_list_block(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ordered_list)

    def test_heading_with_7_hashes_is_paragraph(self):
        block = "####### Too many hashes"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_heading_without_space_after_hashes_is_paragraph(self):
        block = "##No space after hashes"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_code_block_single_line(self):
        block = "```print('inline-ish')```"
        self.assertEqual(block_to_block_type(block), BlockType.code)

    def test_code_block_missing_closing_backticks_is_paragraph(self):
        block = "```py\nprint('hi')"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_quote_with_one_bad_line_becomes_paragraph(self):
        block = "> good line\nnot a quote line"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_unordered_list_with_one_bad_line_becomes_paragraph(self):
        block = "- good\nbad line"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_ordered_list_wrong_start_number_is_paragraph(self):
        block = "2. wrong start\n3. second"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_ordered_list_non_incrementing_is_paragraph(self):
        block = "1. first\n3. skip number"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_paragraph_starting_with_dash_but_no_space(self):
        block = "-Not a list, just text"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_paragraph_starting_with_number_without_dot(self):
        block = "1 This is not a list item"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

if __name__ == "__main__":
    unittest.main()



 # Assuming your function is in markdown_blocks.py

class TestMarkdownToHtml(unittest.TestCase):
    def test_single_paragraph(self):
        md = "This is a simple paragraph."
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><p>This is a simple paragraph.</p></div>"
        )

    def test_paragraph_with_inline(self):
        md = "This is **bold** text and *italic* text."
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><p>This is <b>bold</b> text and <i>italic</i> text.</p></div>"
        )

    def test_multiline_paragraph(self):
        md = """This is a multi-line
paragraph that should
be joined."""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><p>This is a multi-line paragraph that should be joined.</p></div>",
        )

    def test_quote_with_inline(self):
        md = """> This is a quote
> with _italic_ and **bold**."""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>This is a quote with <i>italic</i> and <b>bold</b>.</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """- item one
- item two
- **bold** three"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ul><li>item one</li><li>item two</li><li><b>bold</b> three</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """1. first
2. second
3. third"""
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ol><li>first</li><li>second</li><li>third</li></ol></div>",
        )