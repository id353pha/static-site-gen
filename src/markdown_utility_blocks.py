import re


def markdown_to_blocks(text):
    blank_line_regex = r"(?:\r?\n){2,}"
    blocks = re.split(blank_line_regex, text.strip())
    final_blocks = [block.strip() for block in blocks]
    return final_blocks
