import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnodes_eq(self):
        node = HTMLNode("p", "this is a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "this is a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node2.__repr__(), node.__repr__())

    def test_htmlnodes_not_eq(self):
        node = HTMLNode("p", "this is a paragraph", None, None)
        node2 = HTMLNode("p", "this is a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node2.__repr__(), node.__repr__())

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(" href='https://www.google.com' target='_blank'", node.props_to_html())

if __name__ == "__main__":
    unittest.main()