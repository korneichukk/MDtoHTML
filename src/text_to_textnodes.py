from src.md_links import split_nodes_images, split_nodes_link
from src.split_delimiter import split_nodes_delimiter
from src.textnode import TextNode, TextType


def text_to_textnodes(text: str):
    nodes = split_nodes_delimiter(
        [TextNode(text=text, text_type=TextType.NORMAL_TEXT)],
        delimiter="**",
        text_type=TextType.BOLD_TEXT,
    )
    nodes = split_nodes_delimiter(
        nodes,
        delimiter="__",
        text_type=TextType.BOLD_TEXT,
    )
    nodes = split_nodes_delimiter(
        nodes,
        delimiter="*",
        text_type=TextType.ITALIC_TEXT,
    )
    nodes = split_nodes_delimiter(
        nodes,
        delimiter="_",
        text_type=TextType.ITALIC_TEXT,
    )
    nodes = split_nodes_delimiter(
        nodes,
        delimiter="`",
        text_type=TextType.CODE_TEXT,
    )
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
