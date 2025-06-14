import unittest

from src.leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        tag = "a"
        value = "GOOGLE"
        props = {"href": "https://google.com", "target": "_blank"}
        node = LeafNode(tag=tag, value=value, props=props)

        self.assertEqual(
            node.to_html(),
            f'<a href="{props["href"]}" target="{props["target"]}" >{value}</{tag}>',
        )

    def test_to_html_empty_value(self):
        node = LeafNode(value="", tag="a", props=None)
        self.assertEqual(node.to_html(), "<a></a>")

    def test_to_html_empty_tag(self):
        node = LeafNode(value="asdf", tag=None, props=None)
        self.assertEqual(node.to_html(), "asdf")


if __name__ == "__main__":
    unittest.main()
