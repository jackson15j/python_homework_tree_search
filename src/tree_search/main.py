"""Tree Search Methods."""
from pathlib import Path
from pprint import pprint
import json


class FileNotFound(Exception):
    """File not found exception."""


class RootFundNotFound(Exception):
    """Root Fund not found exception."""


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


def _normalise_data(data: list) -> list:
    """When `Fund <x>` is found, find the version with `holdings`
    and inject back. ie. Funds discovery.
    """
    # Need the root funds names and index in list for later lookup and
    # injection.
    root_funds = {x["name"]: i for i, x in enumerate(data)}

    for fund in data:
        for holding in fund.get("holdings", []):
            if "Fund" in holding["name"]:
                # FIXME: Dirty assumption based off given data that
                # all Funds are `Fund <x>`. This could be fixed up to
                # use the `root_funds` keys.
                holding["holdings"] = data[root_funds[holding["name"]]]["holdings"]
    return data


def _flatten_branch(root_fund: str, data: dict) -> dict:
    raise NotImplementedError


def is_company_under_root_fund(root_fund: str, company: str, data: list) -> bool:
    """Return a if the Company is present in the branch under the
    Root Fund or not.

    :param str root_fund: Root-level fund in the nested structure.
    :param str company: Company to search for under root fund.
    :param list data: Nested structure of Funds/Companies to parse.
    :returns bool:
    """
    root_funds = {x["name"]: i for i, x in enumerate(data)}
    if root_fund not in root_funds.keys():
        return False
    # TODO: Ideally I should search down the structure for the company
    # name, but going to be dirty and convert the everything back to a
    # json string and do a quick string comparison check. - Very
    # dirty, but gets something going quickly. Will Refactor this away
    # very soon!
    json_str = json.dumps(data[root_funds[root_fund]])
    return company in json_str


def get_companies(root_fund: str, data: list) -> list:
    """Return a deduplicated list of Companies that are nested under
    the provided root fund. Sub-funds will not be present in the
    returned Companies list.

    :param str root_fund: Root-level fund in the nested structure.
    :param list data: Nested structure of Funds/Companies to parse.
    :returns list: List of Companies under the root fun.
    """
    root_funds = {x["name"]: i for i, x in enumerate(data)}
    if root_fund not in root_funds.keys():
        raise RootFundNotFound()

    companies = set()
    def recursive_scan(x):
        # TODO: Could pull out the `weights` at the same time to avoid
        # doing another pass when generating the list. It would mean
        # that I can't use `set` to de-dupe the company names, since I
        # need to add all of the multiplied weights for each
        # investment into the Company.
        for holding in x.get("holdings", []):
            if not "Fund" in holding["name"]:
                companies.add(holding["name"])
            recursive_scan(holding)

    recursive_scan(data[root_funds[root_fund]])
    return list(companies)


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
    json_str = _read_file_contents()
    raw_data = _parse_file_contents(json_str)
    pprint(raw_data)
    normalised_data = _normalise_data(raw_data)
    pprint(normalised_data)


if __name__ == "__main__":
    # TODO:
    main()
