import unittest

from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is not a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", text_type_italic)
        node2 = TextNode("This is a text node", text_type_code)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", text_type_italic, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, italic, https://www.boot.dev)", repr(node)
        )

    # def test_node_to_html_node(self):
    #     node = TextNode("This is a link node", text_type_link, "https://www.google.com")
    #     prop = {"href": "https://www.google.com"}
    #     html_node = LeafNode("a", "This is a link node", prop)
    #
    #     self.assertEqual(html_node, text_node_to_html_node(node))


if __name__ == "__main__":
    unittest.main()
