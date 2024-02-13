import os
import sys


def read_banner(file_path):
    """Reads the content of the banner file."""
    with open(file_path, "r") as file:
        return file.read()


def parse_banner(file_content):
    """Parses the banner content into ASCII art for each character."""
    ascii_dict = {}
    for i, art in enumerate(file_content.split("\n\n")):
        char_key = chr(i + 32)
        if char_key > '~':
            break
        ascii_dict[char_key] = art
    return ascii_dict
