def read_banner(file_path):
    """Reads the content of the banner file."""
    with open(file_path, "r") as file:
        return file.read()
