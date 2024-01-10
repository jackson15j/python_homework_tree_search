"""Tests for the main Tree Search methods."""
from pathlib import Path
from src.tree_search.main import (
    _read_file_contents,
    _parse_file_contents,
    _normalise_data,
    is_company_under_root_fund,
    get_companies,
    get_company_percentage_investment,
)

NORMALISED_DATA = _parse_file_contents(_read_file_contents(Path("exp_data.json")))


class TestMain:
    """TODO"""
    def test_is_company_under_root_fund(self):
        assert is_company_under_root_fund(
            "Ethical Global Fund", "GoldenGadgets", NORMALISED_DATA
        ) is True

    def test_is_company_not_under_root_fund(self):
        assert is_company_under_root_fund(
            "Ethical Global Fund", "NonExistantCompany", NORMALISED_DATA
        ) is False

    def test_get_companies(self):
        exp = [
            "MicroFit",
            "GreenCo",
            "GrapeCo",
            "SolarCorp",
            "SpaceY",
            "BeanzRUS",
            "GoldenGadgets",
        ]
        assert get_companies(
            "Ethical Global Fund", NORMALISED_DATA
        ).sort() == exp.sort()

    def test_get_company_percentage_investment(self):
        exp_val = 15
        assert get_company_percentage_investment(
            "Ethical Global Fund", "GoldenGadgets", NORMALISED_DATA
        ) == exp_val

    def test_get_company_percentage_investment_exp_not_found(self):
        assert get_company_percentage_investment(
            "Ethical Global Fund", "NonExistantCompany", NORMALISED_DATA
        ) == 0


class TestMainPrivateFunctions:
    """Attitudes around testing private functions varies between
    people due to the tight coupling to implementation details. Adding
    to get me moving swiftly, but will probably delete once I'm happy
    with the business logic level tests.
    """

    def test__normalise_data(self):
        json_str = _read_file_contents()
        raw_data = _parse_file_contents(json_str)
        assert _normalise_data(raw_data) == _parse_file_contents(_read_file_contents(Path("exp_data.json")))
