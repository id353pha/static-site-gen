import unittest

from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        pass

    def test_prop_to_html(self):
        prop = {"href": "https://www.google.com", "target": "_blank"}
        node = HtmlNode("div", "Hello my man", None, prop)
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', node.props_to_html()
        )


if __name__ == "__main__":
    unittest.main()
