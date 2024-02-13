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


def generate_ascii_art(string_to_convert, ascii_dict):
    """Generates ASCII art for the given string."""
    ascii_art_lines = []
    for line in string_to_convert.split("\\n"):
        ascii_art_for_line = ['' for _ in range(8)]
        for char in line:
            if char in ascii_dict:
                char_art = ascii_dict[char].split("\n")
                for i in range(8):
                    ascii_art_for_line[i] += char_art[i] + " "
        ascii_art_lines.append("\n".join(ascii_art_for_line))
    return "\n".join(ascii_art_lines)


if __name__ == '__main__':
    user_input = sys.argv
    banner_type = ('standard', 'shadow', 'thinkertoy')

    if len(user_input) < 2:
        print("Usage: python main.py 'string_to_convert' 'banner_type'")
        sys.exit(1)

    string_to_parse = user_input[1]
    banner_type = user_input[2] if len(user_input) == 3 and user_input[2] in banner_type else 'standard'

    banner_path = os.path.join("./", f"{banner_type}.txt")
    banner_content = read_banner(banner_path)
    ascii_dict = parse_banner(banner_content)
    ascii_art = generate_ascii_art(string_to_parse, ascii_dict)
    print(ascii_art)
