import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        pass

    def test_to_html(self):
        prop = {"href": "https://www.google.com", "target": "_blank"}
        node = LeafNode("div", "Hello my man", prop)
        self.assertEqual(
            f'<div href="https://www.google.com" target="_blank">Hello my man</div>',
            node.to_html(),
        )

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Test no tag")
        self.assertEqual("Test no tag", node.to_html())


if __name__ == "__main__":
    unittest.main()
