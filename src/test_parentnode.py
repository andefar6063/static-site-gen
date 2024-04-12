import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_of_one_node(self):
        child = LeafNode("p", "this is a paragraph")
        parent = ParentNode("div", [child])
        self.assertEqual("<div><p>this is a paragraph</p></div>", parent.to_html())

    def test_parent_of_many_node(self):
        parent = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", parent.to_html())


    def test_grandparent_node(self):
        child = LeafNode("p", "this is a paragraph")
        parent = ParentNode("div", [child])
        grand_parent = ParentNode("span", [parent])
        self.assertEqual("<span><div><p>this is a paragraph</p></div></span>", grand_parent.to_html())

if __name__ == "__main__":
    unittest.main()