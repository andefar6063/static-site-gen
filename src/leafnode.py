from htmlnode import HTMLNode
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        """
        self.tag - The tag for the value
        self.value - The type of text this node contains, which is just a string like "bold" or "italic"
        self.props - The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
        """
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"