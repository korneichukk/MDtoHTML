import unittest
from src.block_markdown import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic_markdown(self):
        text = (
            "# Header 1\n\n"
            "This is a paragraph with **bold** text.\n\n"
            "- List item 1\n"
            "- List item 2\n\n"
            "Another paragraph."
        )
        expected = [
            "# Header 1",
            "This is a paragraph with **bold** text.",
            "- List item 1\n- List item 2",
            "Another paragraph.",
        ]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_reduce_multiple_newlines_in_markdown(self):
        text = (
            "# Header 1\n\n\n\n"
            "Paragraph with *italic* text.\n\n\n"
            "1. First item\n"
            "2. Second item\n\n\n\n"
            "> Blockquote\n\n\n"
        )
        expected = [
            "# Header 1",
            "Paragraph with *italic* text.",
            "1. First item\n2. Second item",
            "> Blockquote",
        ]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_leading_trailing_spaces_in_markdown(self):
        text = (
            "  ## Header 2  \n\n"
            "  Paragraph with code `print('hello')`  \n\n\n"
            "  - Item A  \n"
            "  - Item B  \n\n"
            "  > Another blockquote  "
        )
        expected = [
            "## Header 2",
            "Paragraph with code `print('hello')`",
            "- Item A\n- Item B",
            "> Another blockquote",
        ]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_empty_string(self):
        text = ""
        expected = [""]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_only_newlines(self):
        text = "\n\n\n\n"
        expected = [""]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_single_block_markdown(self):
        text = "Simple paragraph with **bold** and _italic_ text."
        expected = ["Simple paragraph with **bold** and _italic_ text."]
        self.assertEqual(markdown_to_blocks(text), expected)


if __name__ == "__main__":
    unittest.main()
