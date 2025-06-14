from typing import Any, Dict, Optional

from src.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        value: str,
        tag: Optional[str] = None,
        props: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode value cannot be empty.")

        if not self.tag:
            return self.value

        result = f"<{self.tag}{self.props_to_html()}>{self.value}"
        if self.tag != "img":
            result += f"</{self.tag}>"

        return result
