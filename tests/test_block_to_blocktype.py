import unittest
from src.block_markdown import markdown_to_blocks, block_to_blocktype, BlockType


class TestMarkdownParser(unittest.TestCase):
    def test_markdown_to_blocks_basic(self):
        md = "# Heading\n\nParagraph text.\n\n\n\n- Item 1\n- Item 2"
        expected = ["# Heading", "Paragraph text.", "- Item 1\n- Item 2"]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_heading_detection(self):
        block = "# This is a heading"
        self.assertEqual(block_to_blocktype(block), BlockType.HEADING)

    def test_code_block_detection(self):
        block = "```python\nprint('Hello')\n```"
        self.assertEqual(block_to_blocktype(block), BlockType.CODE)

    def test_quote_block_detection(self):
        block = "> This is a quote\n> with multiple lines"
        self.assertEqual(block_to_blocktype(block), BlockType.QUOTE)

    def test_unordered_list_detection(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_blocktype(block), BlockType.UNORDERED_LIST)

    def test_ordered_list_detection(self):
        block = "1. First\n2. Second\n4. Fourth"
        self.assertEqual(block_to_blocktype(block), BlockType.ORDERED_LIST)

    def test_ordered_list_invalid_sequence(self):
        block = "1. One\n2. Two\n1. Again One"
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

    def test_paragraph_detection(self):
        block = "This is just a normal paragraph.\nIt has multiple lines."
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

    def test_invalid_code_block(self):
        block = "```\nUnclosed code block"
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

    def test_invalid_quote_block(self):
        block = "> Valid line\nNot a quote"
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

    def test_unordered_list_with_extra_spaces(self):
        block = "-  Item 1\n  -  Item 2"
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

    def test_mixed_block_defaults_to_paragraph(self):
        block = "# Heading\n- List item\n> Quote"
        self.assertEqual(block_to_blocktype(block), BlockType.HEADING)

    def test_markdown_to_blocks_with_extra_spaces_and_newlines(self):
        md = "  # Header 1  \n\n\n  > Quote line\n\n\n\n1. One\n2. Two\n\n\nParagraph"
        blocks = markdown_to_blocks(md)
        expected = ["# Header 1", "> Quote line", "1. One\n2. Two", "Paragraph"]
        self.assertEqual(blocks, expected)


if __name__ == "__main__":
    unittest.main()
