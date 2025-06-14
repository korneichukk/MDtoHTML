import unittest

from src.textnode import TextNode, TextType


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_textnode_to_htmlnode(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        html_node = node.textnode_to_htmlnode()
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_bold_textnode_to_htmlnode(self):
        node = TextNode("Bold", TextType.BOLD_TEXT)
        html_node = node.textnode_to_htmlnode()
        self.assertEqual(html_node.to_html(), "<b>Bold</b>")

    def test_italic_textnode_to_htmlnode(self):
        node = TextNode("Italic", TextType.ITALIC_TEXT)
        html_node = node.textnode_to_htmlnode()
        self.assertEqual(html_node.to_html(), "<i>Italic</i>")

    def test_code_textnode_to_htmlnode(self):
        node = TextNode("print('hi')", TextType.CODE_TEXT)
        html_node = node.textnode_to_htmlnode()
        self.assertEqual(html_node.to_html(), "<code>print('hi')</code>")

    def test_link_textnode_to_htmlnode(self):
        node = TextNode("Click here", TextType.LINK, url="https://example.com")
        html_node = node.textnode_to_htmlnode()
        self.assertEqual(
            html_node.to_html(), '<a href="https://example.com" >Click here</a>'
        )

    def test_image_textnode_to_htmlnode(self):
        node = TextNode(
            text="Image alt text",
            text_type=TextType.IMAGE,
            url="https://example.com/image.png",
        )
        html_node = node.textnode_to_htmlnode()
        self.assertEqual(
            html_node.to_html(),
            '<img src="https://example.com/image.png" alt="Image alt text" >',
        )
