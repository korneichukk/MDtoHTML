import unittest

from src.textnode import TextType, TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a link node", TextType.LINK, "https://google.com")
        node2 = TextNode("This is a link node 2", TextType.LINK, "https://google.com")
        self.assertNotEqual(node, node2)

    def test_empty_link_eq(self):
        node = TextNode("This is a link node", TextType.LINK, "https://google.com")
        node2 = TextNode("This is a link node 2", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_different_text_type_eq(self):
        node = TextNode("This is a link node", TextType.LINK, "https://google.com")
        node2 = TextNode("This is a link node", TextType.NORMAL_TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
