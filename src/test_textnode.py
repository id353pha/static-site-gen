import unittest

from leafnode import LeafNode
from textnode import (
    TextNode,
    split_nodes_delimiter,
    text_node_to_html_node,
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

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
