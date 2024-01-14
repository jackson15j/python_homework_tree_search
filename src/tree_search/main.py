"""Tree Search Methods."""
from pathlib import Path
import json
from tree_search.depth_first_search_stack import dfs

ROOT_FUND = "Ethical Global Fund"
ROGUE_COMPANY = "GoldenGadgets"


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


def get_unique_companies_without_funds(weighted_funds: dict[str, float]) -> list:
    return [x for x in weighted_funds if "Fund" not in x]


def main():
    json_str = read_file_contents()
    raw_data = parse_file_contents(json_str)
    output = dfs(raw_data, "Ethical Global Fund")
    companies = get_unique_companies_without_funds(output)
    # Answer: [
    #     'GrapeCo', 'BeanzRUS', 'SpaceY', 'SolarCorp',
    #     'GoldenGadgets', 'GreenCo', 'MicroFit'
    # ]
    print(
        f"List of all Companies (minus Funds!), under root Fund:\n\t"
        f"{ROOT_FUND!r}: {companies}"
    )
    # Answer: True, 15.0%.
    print(
        f"Is {ROGUE_COMPANY!r} under {ROOT_FUND!r}?:\n\t"
        f"{ROGUE_COMPANY in companies}.\n"
        f"...And if so, what percentage of investment has gone to "
        f"{ROGUE_COMPANY!r}?:\n\t"
        f"{output.get(ROGUE_COMPANY, 0) * 100}%"
    )

if __name__ == "__main__":
    main()
