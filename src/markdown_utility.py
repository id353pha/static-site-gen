import re

from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
)

text_types = ["text", "bold", "italic", "code", "link", "image"]


def text_to_textnodes(text):
    starting_list = [TextNode(text, text_type_text)]
    list_nodes = split_nodes_delimiter(starting_list, "**", text_type_bold)
    list_nodes = split_nodes_delimiter(list_nodes, "*", text_type_italic)
    list_nodes = split_nodes_delimiter(list_nodes, "`", text_type_code)
    list_nodes = split_nodes_image(list_nodes)
    list_nodes = split_nodes_link(list_nodes)
    return list_nodes


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


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
        else:
            temp_nodes = []
            images = extract_markdown_images(old_node.text)
            text = old_node.text
            if len(images) == 0:
                new_nodes.append(old_node)
                continue
            for image in images:
                split_text = text.split(f"![{image[0]}]({image[1]})", 1)
                if len(split_text) != 2:
                    raise ValueError("Invalid markdown, formatted section not closed")
                text = split_text[1]
                if split_text[0] != "":
                    temp_nodes.append(TextNode(split_text[0], text_type_text))
                temp_nodes.append(TextNode(image[0], text_type_image, image[1]))
            new_nodes.extend(temp_nodes)
            if text != "":
                new_nodes.append(TextNode(text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
        else:
            temp_nodes = []
            links = extract_markdown_link(old_node.text)
            text = old_node.text
            if len(links) == 0:
                new_nodes.append(old_node)
                continue
            for link in links:
                split_text = text.split(f"[{link[0]}]({link[1]})", 1)
                if len(split_text) != 2:
                    raise ValueError("Invalid markdown, formatted section not closed")
                text = split_text[1]
                if split_text[0] != "":
                    temp_nodes.append(TextNode(split_text[0], text_type_text))
                temp_nodes.append(TextNode(link[0], text_type_link, link[1]))
            new_nodes.extend(temp_nodes)
            if text != "":
                new_nodes.append(TextNode(text, text_type_text))
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_link(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches
