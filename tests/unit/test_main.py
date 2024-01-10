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


class TestMain:
    """TODO"""
    def test_is_company_under_root_fund(self):
        # TODO: Update `data` to match expected output.
        data = {"a": [{"b": {}}]}
        assert is_company_under_root_fund("a", "b", data) is True

    def test_is_company_not_under_root_fund(self):
        # TODO: Update `data` to match expected output.
        data = {"a": [{"b": {}}]}
        assert is_company_under_root_fund("a", "c", data) is False

    def test_get_companies(self):
        # TODO: Update `data` to match expected output.
        data = {"a": [{"b": {}}, {"c": {}}]}
        assert get_companies("a", data) == ["b", "c"]

    def test_get_company_percentage_investment(self):
        # TODO: Update `data` to match expected output.
        exp_val = 12.34
        data = {"a": {"b": exp_val}}
        assert get_company_percentage_investment("a", "b", data) == exp_val

    def test_get_company_percentage_investment_exp_not_found(self):
        # TODO: Update `data` to match expected output.
        data = {"a": {}}
        assert get_company_percentage_investment("a", "c", data) == 0


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
