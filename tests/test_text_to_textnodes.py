import unittest
from src.textnode import TextNode, TextType
from src.text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_complex_text_parsing(self):
        input_text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![image](https://i.imgur.com/ssss.jpeg) "
            "and a [link](https://google.com)"
        )

        expected_nodes = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.NORMAL_TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/ssss.jpeg"),
            TextNode(" and a ", TextType.NORMAL_TEXT),
            TextNode("link", TextType.LINK, "https://google.com"),
        ]

        actual_nodes = text_to_textnodes(input_text)

        self.assertEqual(len(actual_nodes), len(expected_nodes))
        for actual, expected in zip(actual_nodes, expected_nodes):
            self.assertEqual(actual.text, expected.text)
            self.assertEqual(actual.text_type, expected.text_type)
            self.assertEqual(actual.url, expected.url)

    def test_multiple_links_and_images(self):
        input_text = (
            "See [Google](https://google.com) and ![Logo](https://logo.com/img.png) "
            "and another [GitHub](https://github.com)"
        )
        expected_nodes = [
            TextNode("See ", TextType.NORMAL_TEXT),
            TextNode("Google", TextType.LINK, "https://google.com"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("Logo", TextType.IMAGE, "https://logo.com/img.png"),
            TextNode(" and another ", TextType.NORMAL_TEXT),
            TextNode("GitHub", TextType.LINK, "https://github.com"),
        ]
        actual_nodes = text_to_textnodes(input_text)

        self.assertEqual(len(actual_nodes), len(expected_nodes))
        for actual, expected in zip(actual_nodes, expected_nodes):
            self.assertEqual(actual.text, expected.text)
            self.assertEqual(actual.text_type, expected.text_type)
            self.assertEqual(actual.url, expected.url)

    def test_code_text(self):
        input_text = "Here is some `inline code` in a sentence"
        expected_nodes = [
            TextNode("Here is some ", TextType.NORMAL_TEXT),
            TextNode("inline code", TextType.CODE_TEXT),
            TextNode(" in a sentence", TextType.NORMAL_TEXT),
        ]
        actual_nodes = text_to_textnodes(input_text)

        self.assertEqual(len(actual_nodes), len(expected_nodes))
        for actual, expected in zip(actual_nodes, expected_nodes):
            self.assertEqual(actual.text, expected.text)
            self.assertEqual(actual.text_type, expected.text_type)
            self.assertEqual(actual.url, expected.url)

    def test_bold_text_with_double_asterisks_and_underscores(self):
        input_text = "This is **bold** and also __bold__"
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" and also ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
        ]
        actual_nodes = text_to_textnodes(input_text)

        self.assertEqual(len(actual_nodes), len(expected_nodes))
        for actual, expected in zip(actual_nodes, expected_nodes):
            self.assertEqual(actual.text, expected.text)
            self.assertEqual(actual.text_type, expected.text_type)
            self.assertEqual(actual.url, expected.url)

    def test_italic_text_with_single_asterisks_and_underscores(self):
        input_text = "This is *italic* and also _italic_"
        expected_nodes = [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" and also ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
        ]
        actual_nodes = text_to_textnodes(input_text)

        self.assertEqual(len(actual_nodes), len(expected_nodes))
        for actual, expected in zip(actual_nodes, expected_nodes):
            self.assertEqual(actual.text, expected.text)
            self.assertEqual(actual.text_type, expected.text_type)
            self.assertEqual(actual.url, expected.url)


if __name__ == "__main__":
    unittest.main()
