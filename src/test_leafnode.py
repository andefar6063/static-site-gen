import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node(self):
        leaf_node = LeafNode("p", "this is a paragraph", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual("<p href='https://www.google.com' target='_blank'>this is a paragraph</p>", leaf_node.to_html())

if __name__ == "__main__":
    unittest.main()