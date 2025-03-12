def read_file(path: str) -> str:
    """Reads the text content from a file."""
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(path: str, content: str) -> None:
    """Saves text content to a file."""
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
