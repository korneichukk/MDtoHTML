import re
from enum import Enum
from typing import List


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown: str):
    markdown = re.sub(r"\n{3,}", "\n\n", markdown.strip())
    cleaned_blocks = []
    for block in markdown.split("\n\n"):
        lines = block.split("\n")
        stripped_lines = [line.strip() for line in lines]
        cleaned_blocks.append("\n".join(stripped_lines))

    return cleaned_blocks


def line_have_increasing_order(block: str) -> bool:
    prev_number = -1
    for line in block.splitlines():
        m = re.match(r"^\s*(\d+)\.", line)
        if not m:
            return False
        try:
            number = int(m.group(1))
            if number <= prev_number:
                return False
            prev_number = number
        except Exception:
            return False

    return True


def block_to_blocktype(block: str) -> BlockType:
    heading_block = re.match(r"^(#){1,6} (.+)", block)
    if heading_block:
        return BlockType.HEADING

    code_block = re.match(r"^```(\w*).*?```$", block, flags=re.DOTALL)
    if code_block:
        return BlockType.CODE

    quote_block = re.fullmatch(r"(>.*\n?)+", block)
    if quote_block:
        return BlockType.QUOTE

    quote_ul = re.fullmatch(r"(- +.*\n?)+", block)
    if quote_ul:
        return BlockType.UNORDERED_LIST

    if line_have_increasing_order(block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
