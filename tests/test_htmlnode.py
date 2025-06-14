import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr_full_values(self):
        tag = "a"
        link_text = "GOOGLE"
        children = None
        props = {"href": "https://google.com", "target": "_blank"}
        node = HTMLNode(tag, link_text, children, props)

        self.assertEqual(
            str(node),
            f'HTMLNode(tag={tag}, value={link_text}, children={children}, props= href="https://google.com" target="_blank" )',
        )

    def test_repr_empty_values(self):
        tag = None
        link_text = None
        children = None
        props = None
        node = HTMLNode(tag, link_text, children, props)

        self.assertEqual(
            str(node),
            f"HTMLNode(tag={tag}, value={link_text}, children={children}, props=)",
        )


if __name__ == "__main__":
    unittest.main()
