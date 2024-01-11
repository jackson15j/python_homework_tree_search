"""Tree Search Methods."""
from pathlib import Path
import json


class FileNotFound(Exception):
    """File not found exception."""


def read_file_contents(filepath: Path = Path("data.json")) -> str:
    """Reads file contents to a string.

    :param pathlib.Path filepath: file to read.
    :returns: str.
    :raises: FileNotFound.
    """
    if not filepath.exists():
        raise FileNotFound(f"{filepath} does not exist!")
    return filepath.read_text()


def parse_file_contents(json_str: str) -> dict:
    """Parse JSON Str to a python dict.

    :param str json_str:
    :returns: dict.
    """
    return json.loads(json_str)


def main():
    # TODO: Call each function in-turn to get final output.
    json_str = read_file_contents()
    raw_data = parse_file_contents(json_str)


if __name__ == "__main__":
    main()
