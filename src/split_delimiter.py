from typing import List

from src.textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: List[TextNode], delimiter: str, text_type: TextType
):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(old_node)
            continue

        old_node_splitted = old_node.text.split(delimiter)
        for i, old_node_splitted_item in enumerate(old_node_splitted):
            if i % 2 == 0:
                new_nodes.append(
                    TextNode(text=old_node_splitted_item, text_type=old_node.text_type)
                )
            else:
                new_nodes.append(
                    TextNode(text=old_node_splitted_item, text_type=text_type)
                )

    return new_nodes
