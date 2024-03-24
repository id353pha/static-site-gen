import functools


class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is not None:
            return functools.reduce(
                lambda a, b: a + b,
                map(lambda item: f' {item[0]}="{item[1]}"', self.props.items()),
            )
        return ""

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"
