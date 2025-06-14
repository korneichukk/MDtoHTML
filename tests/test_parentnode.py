import unittest

from src.parentnode import ParentNode
from src.leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_parent_node(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_empty_parent_node(self):
        node = ParentNode(tag="div", children=[])
        self.assertRaises(ValueError, node.to_html)

    def test_parent_node_with_only_leaf_nodes(self):
        node = ParentNode(
            tag="span",
            children=[
                LeafNode(tag=None, value="Just text "),
                LeafNode(tag="strong", value="strong text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<span>Just text <strong>strong text</strong></span>",
        )

    def test_nested_parent_nodes(self):
        node = ParentNode(
            tag="div",
            children=[
                LeafNode(tag=None, value="Start"),
                ParentNode(
                    tag="ul",
                    children=[
                        LeafNode(tag="li", value="Item 1"),
                        LeafNode(tag="li", value="Item 2"),
                    ],
                ),
                LeafNode(tag=None, value="End"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div>Start<ul><li>Item 1</li><li>Item 2</li></ul>End</div>",
        )

    def test_single_leaf_child(self):
        node = ParentNode(
            tag="section",
            children=[LeafNode(tag="h1", value="Title")],
        )
        self.assertEqual(node.to_html(), "<section><h1>Title</h1></section>")

    def test_all_none_tag_leaf_nodes(self):
        node = ParentNode(
            tag="article",
            children=[
                LeafNode(tag=None, value="This "),
                LeafNode(tag=None, value="is "),
                LeafNode(tag=None, value="plain text."),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<article>This is plain text.</article>",
        )
