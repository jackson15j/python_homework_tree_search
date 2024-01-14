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
    """Return a list of companies with the Fund names stripped out.

    :param dict[str, float] weighted_funds: dict of Company/Fund names
        as the key and cumulative weights as the values.
    :returns list: List of company names (minus fund names).
    """
    # NOTE: This obviously relies on the Funds having `Fund` in their
    # name. Without this assumption, I would have to look at the
    # original data and keep a set (python's de-duped list built-in)
    # of all names that had a `holdings` key aswell. Then I could
    # create a new list by checking the name is not in the list of
    # Fund names.
    return [x for x in weighted_funds if "Fund" not in x]


def is_company_under_fund(fund_data: dict[str, float], company: str) -> bool:
    """Return bool of company in list under the Fund data.

    :param dict[str, float] fund_data: dict of Company/Fund names
        as the key and cumulative weights as the values.
    :param str company: Company to check presence for.
    :returns bool:
    """
    return company in fund_data


def get_company_investment_percentage_under_fund(
        fund_data: dict[str, float], company: str
) -> float:
    """Return percentage of investment into company under the Fund.

    :param dict[str, float] fund_data: dict of Company/Fund names
        as the key and cumulative weights as the values.
    :param str company: Company to get investment percentage for.
    :returns float:
    """
    return fund_data.get(company, 0.0) * 100


def main():
    json_str = read_file_contents()
    raw_data = parse_file_contents(json_str)
    output = dfs(raw_data, "Ethical Global Fund")
    print("DEBUG: Cumulative weights for each Fund/Company: ", output)
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
        f"{is_company_under_fund(output, ROGUE_COMPANY)}.\n"
        f"...And if so, what percentage of investment has gone to "
        f"{ROGUE_COMPANY!r}?:\n\t"
        f"{get_company_investment_percentage_under_fund(output, ROGUE_COMPANY)}%"
    )

if __name__ == "__main__":
    main()
