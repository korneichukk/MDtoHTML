import unittest

from src.md_links import split_nodes_link, split_nodes_imags
from src.textnode import TextNode, TextType


class TestMarkdownExtract(unittest.TestCase):
    def test_split_link(self):
        node = TextNode(
            "This is text with a [link](https://google.com) and another [second link](https://cisco.com)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL_TEXT),
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode(" and another ", TextType.NORMAL_TEXT),
                TextNode("second link", TextType.LINK, "https://cisco.com"),
            ],
            new_nodes,
        )

    def test_split_link_no_links(self):
        node = TextNode("Just plain text with no links here.", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_link_surrounded_by_text(self):
        node = TextNode(
            "Before [link](https://example.com) after.", TextType.NORMAL_TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Before ", TextType.NORMAL_TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" after.", TextType.NORMAL_TEXT),
            ],
            new_nodes,
        )

    def test_split_image(self):
        node = TextNode(
            "Here is an image ![alt](https://img.com/pic.png) in text",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_imags([node])
        self.assertListEqual(
            [
                TextNode("Here is an image ", TextType.NORMAL_TEXT),
                TextNode("alt", TextType.IMAGE, "https://img.com/pic.png"),
                TextNode(" in text", TextType.NORMAL_TEXT),
            ],
            new_nodes,
        )

    def test_split_image_no_images(self):
        node = TextNode("Text with no images at all.", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_imags([node])
        self.assertListEqual([node], new_nodes)

    def test_link_inside_image_ignored(self):
        node = TextNode(
            "Here is a link [text](https://link.com) and an image ![img](https://img.com)",
            TextType.NORMAL_TEXT,
        )
        image_nodes = split_nodes_imags([node])
        self.assertListEqual(
            [
                TextNode(
                    "Here is a link [text](https://link.com) and an image ",
                    TextType.NORMAL_TEXT,
                ),
                TextNode("img", TextType.IMAGE, "https://img.com"),
            ],
            image_nodes,
        )

        link_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Here is a link ", TextType.NORMAL_TEXT),
                TextNode("text", TextType.LINK, "https://link.com"),
                TextNode(" and an image ![img](https://img.com)", TextType.NORMAL_TEXT),
            ],
            link_nodes,
        )


if __name__ == "__main__":
    unittest.main()
