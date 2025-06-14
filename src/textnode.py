from enum import Enum
from typing import Optional

from src.leafnode import LeafNode


class TextType(Enum):
    NORMAL_TEXT = "normal_text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(
        self, text: str, text_type: TextType, url: Optional[str] = None
    ) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, TextNode):
            return False

        return (
            self.text == value.text
            and self.text_type == value.text_type
            and self.url == value.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def textnode_to_htmlnode(self):
        if self.text_type == TextType.NORMAL_TEXT:
            return LeafNode(value=self.text)
        elif self.text_type == TextType.BOLD_TEXT:
            return LeafNode(tag="b", value=self.text)
        elif self.text_type == TextType.ITALIC_TEXT:
            return LeafNode(tag="i", value=self.text)
        elif self.text_type == TextType.CODE_TEXT:
            return LeafNode(tag="code", value=self.text)
        elif self.text_type == TextType.LINK:
            return LeafNode(tag="a", value=self.text, props={"href": self.url})
        elif self.text_type == TextType.IMAGE:
            return LeafNode(
                tag="img", value="", props={"src": self.url, "alt": self.text}
            )

        raise ValueError(f"{self.text_type} is not among the allowed TextTypes.")
