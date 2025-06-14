from typing import Any, Dict, List, Optional

from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: List,
        props: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("ParentNode tag cannot be empty.")

        if not self.children:
            raise ValueError("ParentNode children cannot be empty")

        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"

        return result
