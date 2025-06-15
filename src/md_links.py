import re
from typing import Callable, List, Union

from src.textnode import TextNode, TextType


def extract_markdown_images(text: str):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)

    result = []
    for match in matches:
        result.append((match[0], match[1]))

    return result


def extract_markdown_links(text: str):
    pattern = r"(?<!\!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)

    result = []
    for match in matches:
        result.append((match[0], match[1]))

    return result


def extract_markdown(
    extract_function: Callable,
    text_type: TextType,
    old_nodes: List[TextNode],
    pattern: str,
):
    result = []
    for old_node in old_nodes:
        split_old_nodes = re.split(pattern, old_node.text)
        old_node_extracted_items = extract_function(old_node.text)

        for i in range(len(split_old_nodes)):
            if i < len(split_old_nodes):
                if not split_old_nodes[i]:
                    continue
                result.append(TextNode(split_old_nodes[i], old_node.text_type))
            if i < len(old_node_extracted_items):
                result.append(
                    TextNode(
                        old_node_extracted_items[i][0],
                        text_type,
                        old_node_extracted_items[i][1],
                    )
                )

    return result


def split_nodes_link(old_nodes: List[TextNode]):
    link_pattern = r"(?<!\!)\[.*?\]\(.*?\)"
    return extract_markdown(
        extract_markdown_links, TextType.LINK, old_nodes, link_pattern
    )


def split_nodes_imags(old_nodes: List[TextNode]):
    image_pattern = r"!\[.*?\]\(.*?\)"
    return extract_markdown(
        extract_markdown_images, TextType.IMAGE, old_nodes, image_pattern
    )
