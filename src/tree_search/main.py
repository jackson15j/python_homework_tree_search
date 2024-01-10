"""Tree Search Methods."""
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
