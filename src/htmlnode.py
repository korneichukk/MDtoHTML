from typing import Any, Dict, List, Optional


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[List["HTMLNode"]] = None,
        props: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html is not implemented in HTMLNode class.")

    def props_to_html(self) -> str:
        if not self.props:
            return ""

        html_props = []
        for prop, value in self.props.items():
            html_props.append(f'{prop}="{value}"')

        return f" {' '.join(html_props)} "

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props_to_html()})"
