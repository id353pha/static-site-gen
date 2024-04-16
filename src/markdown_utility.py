import re

from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_text,
)

text_types = ["text", "bold", "italic", "code", "link", "image"]


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
        else:
            if text_type not in text_types:
                raise ValueError(
                    f"Text type {text_type} does not match any valid markdown type"
                )
            temp_nodes = []
            split_text = old_node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("Invalid markdown, formatted section not closed")
            for i in range(len(split_text)):
                if split_text[i] == "":
                    continue
                if i % 2 != 0:
                    temp_nodes.append(TextNode(split_text[i], text_type))
                else:
                    temp_nodes.append(TextNode(split_text[i], text_type_text))

            new_nodes.extend(temp_nodes)

    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_link(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches
