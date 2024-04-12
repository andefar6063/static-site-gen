from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        """
        self.tag - The parent tag for all children
        self.children - A list containing all children and or grandchildren
        self.props - The URL of the link or image for the parent tag. Default to None if nothing is passed in.
        """
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no value")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        to_html_string_start = f"<{self.tag}{self.props_to_html()}>"
        to_html_string_end = f"</{self.tag}>"
        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return to_html_string_start + children_html + to_html_string_end
        
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.children}, {self.props})"