import unittest
from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        content = "# Hello"
        result = extract_title(content)

        self.assertEqual(result, "Hello")

    def test_uses_first_h1_only(self):
        content = "# First\n# Second"
        result = extract_title(content)
        self.assertEqual(result, "First")


    def test_trims_whitespace(self):
        content = "#  Hello  "
        result = extract_title(content)
        self.assertEqual(result, "Hello")

    def test_raises_without_h1(self):
        content = " Hello"
        with self.assertRaises(Exception):
            extract_title(content)


