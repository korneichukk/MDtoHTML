import unittest

from src.textnode import TextNode, TextType
from src.split_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_single_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        expected = [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_multiple_code_blocks(self):
        node = TextNode("A `code` and another `snippet`", TextType.NORMAL_TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        expected = [
            TextNode("A ", TextType.NORMAL_TEXT),
            TextNode("code", TextType.CODE_TEXT),
            TextNode(" and another ", TextType.NORMAL_TEXT),
            TextNode("snippet", TextType.CODE_TEXT),
            TextNode("", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_no_delimiters(self):
        node = TextNode("No formatting here", TextType.NORMAL_TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        expected = [
            TextNode("No formatting here", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_preserves_non_normal_nodes(self):
        node1 = TextNode("Text with `code`", TextType.NORMAL_TEXT)
        node2 = TextNode("Bold text", TextType.BOLD_TEXT)
        result = split_nodes_delimiter([node1, node2], "`", TextType.CODE_TEXT)
        expected = [
            TextNode("Text with ", TextType.NORMAL_TEXT),
            TextNode("code", TextType.CODE_TEXT),
            TextNode("", TextType.NORMAL_TEXT),
            TextNode("Bold text", TextType.BOLD_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_unmatched_delimiter(self):
        node = TextNode("Unmatched `delimiter test", TextType.NORMAL_TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        expected = [
            TextNode("Unmatched ", TextType.NORMAL_TEXT),
            TextNode("delimiter test", TextType.CODE_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_double_asterisks_bold(self):
        node = TextNode("This is **bold** text", TextType.NORMAL_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        expected = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_double_underscore_bold(self):
        node = TextNode("Also __bold__ text", TextType.NORMAL_TEXT)
        result = split_nodes_delimiter([node], "__", TextType.BOLD_TEXT)
        expected = [
            TextNode("Also ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_single_asterisk_italic(self):
        node = TextNode("This is *italic* text", TextType.NORMAL_TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC_TEXT)
        expected = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_single_underscore_italic(self):
        node = TextNode("Another _italic_ example", TextType.NORMAL_TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        expected = [
            TextNode("Another ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" example", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_multiple_bold_italic(self):
        node = TextNode(
            "Mix **bold1** and *italic1* and __bold2__ and _italic2_",
            TextType.NORMAL_TEXT,
        )
        result = []
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        result = split_nodes_delimiter(result, "*", TextType.ITALIC_TEXT)
        result = split_nodes_delimiter(result, "__", TextType.BOLD_TEXT)
        result = split_nodes_delimiter(result, "_", TextType.ITALIC_TEXT)
        expected = [
            TextNode("Mix ", TextType.NORMAL_TEXT),
            TextNode("bold1", TextType.BOLD_TEXT),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("italic1", TextType.ITALIC_TEXT),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("bold2", TextType.BOLD_TEXT),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("italic2", TextType.ITALIC_TEXT),
            TextNode("", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
