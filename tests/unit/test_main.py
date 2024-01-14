"""Tests for the main Tree Search methods."""
from src.tree_search.main import (
    get_company_investment_percentage_under_fund,
    get_unique_companies_without_funds,
    is_company_under_fund,
    parse_file_contents,
    read_file_contents,
)

DATA = parse_file_contents(read_file_contents())
EXP_WEIGHTINGS = {
    'Ethical Global Fund': 1,
    'GrapeCo': 0.347,
    'Fund D': 0.35,
    'BeanzRUS': 0.21,
    'SpaceY': 0.105,
    'Fund E': 0.035,
    'SolarCorp': 0.028,
    'Fund C': 0.5,
    'GoldenGadgets': 0.15,
    'Fund B': 0.2,
    'GreenCo': 0.06,
    'MicroFit': 0.1,
}
EXP_COMPANY_WEIGHTINGS = {
    'GrapeCo': 0.347,
    'BeanzRUS': 0.21,
    'SpaceY': 0.105,
    'SolarCorp': 0.028,
    'GoldenGadgets': 0.15,
    'GreenCo': 0.06,
    'MicroFit': 0.1,
}
EXP_COMPANIES = [
    'GrapeCo',
    'BeanzRUS',
    'SpaceY',
    'SolarCorp',
    'GoldenGadgets',
    'GreenCo',
    'MicroFit',
]


class TestMain:
    def test_get_unique_companies_without_funds(self):
        assert (
            get_unique_companies_without_funds(EXP_WEIGHTINGS).sort()
            == EXP_COMPANIES.sort()
        )

    def test_is_golden_gadgets_under_ethical_global_fund(self):
        assert (
            is_company_under_fund(EXP_WEIGHTINGS, "GoldenGadgets")
            is True
        )

    def test_what_percentage_of_investment_is_in_golden_gadgets(self):
        assert get_company_investment_percentage_under_fund(
            EXP_WEIGHTINGS, "GoldenGadgets"
        ) == 15.0
