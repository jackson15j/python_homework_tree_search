"""Tree Search Methods."""
from pathlib import Path
import json


class FileNotFound(Exception):
    """File not found exception."""


def _read_file_contents(filepath: Path = Path("data.json")) -> str:
    """Reads file contents to a string.

    :param pathlib.Path filepath: file to read.
    :returns: str.
    :raises: FileNotFound.
    """
    if not filepath.exists():
        raise FileNotFound(f"{filepath} does not exist!")
    return filepath.read_text()


def _parse_file_contents(json_str: str) -> dict:
    """Parse JSON Str to a python dict.

    :param str json_str:
    :returns: dict.
    """
    return json.loads(json_str)


def _normalise_data(data: dict) -> dict:
    raise NotImplementedError


def _flatten_branch(root_fund: str, data: dict) -> dict:
    raise NotImplementedError


def is_company_under_root_fund(root_fund: str, company: str, data: dict) -> bool:
    """Return a if the Company is present in the branch under the
    Root Fund or not.

    :param str root_fund: Root-level fund in the nested structure.
    :param str company: Company to search for under root fund.
    :param dict data: Nested structure of Funds/Companies to parse.
    :returns bool:
    """
    # TODO: add data parsing logic.
    return False


def get_companies(root_fund: str, data: dict) -> list:
    """Return a deduplicated list of Companies that are nested under
    the provided root fund. Sub-funds will not be present in the
    returned Companies list.

    :param str root_fund: Root-level fund in the nested structure.
    :param dict data: Nested structure of Funds/Companies to parse.
    :returns list: List of Companies under the root fun.
    """
    # TODO: add data parsing logic.
    return []


def get_company_percentage_investment(root_fund: str, company: str, data: dict) -> float:
    """Returns the percentage investment of the Company in the branch
    under the Root Fund.

    :param str root_fund: Root-level fund in the nested structure.
    :param str company: Company to search for under root fund.
    :param dict data: Nested structure of Funds/Companies to parse.
    :returns float: Percentage of investment. Returns 0 if Company is
        not under the Root Fund.
    """
    if not is_company_under_root_fund(root_fund, company, data):
        return 0
    # TODO: add data parsing logic.
    return 0


def main():
    # TODO: Call each function in-turn to get final output.
    pass


if __name__ == "__main__":
    # TODO:
    main()
