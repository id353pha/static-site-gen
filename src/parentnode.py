from htmlnode import HtmlNode


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Can't convert to html with no tag property")
        if self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode needs at least one children node")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
