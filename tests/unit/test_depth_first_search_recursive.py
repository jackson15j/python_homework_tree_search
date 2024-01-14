"""Tests for a Depth First Search Solution via recursion."""
from src.tree_search.depth_first_search_recursive import (
    convert_jsonl_to_graph_format,
    dfs,
)
from src.tree_search.main import (
    read_file_contents,
    parse_file_contents,
)

DATA = parse_file_contents(read_file_contents())


class TestDepthFirstSearchRecursive:
    def test_depth_first_search_simple_graph(self):
        """Initial test to do DFS on an arbitrary graph that mimics
        expected graph internals.
        """
        graph = {
            "A": [{"name": "B", "weight": 0.2}, {"name": "C", "weight": 0.8}],
            "B": [{"name": "C", "weight": 0.3}, {"name": "D", "weight": 0.7}],
            "D": [{"name": "C", "weight": 0.5}, {"name": "E", "weight": 0.5}],
        }
        exp = {
            "A": 1,
            "B": 0.2,
            "C": 0.93,
            "D": 0.14,
            "E": 0.07,
        }
        ret_val = {}
        # TODO: Fix state caching in recursive function, between runs.
        # ie. avoid having to explicitly reset all inputs!
        dfs(graph, "A", decimals=2, multiplier=1, ret_val=ret_val)
        assert ret_val == exp

    def test_depth_first_search_simple_graph_that_mimics_expected_data(self):
        """Test DFS on an arbitrary graph that more closely mimics
        expected graph data with Funds having a "holdings" section.
        """
        graph = [
            {"name": "A", "holdings": [{"name": "B", "weight": 0.2}, {"name": "C", "weight": 0.8}]},
            {"name": "B", "holdings": [{"name": "C", "weight": 0.3}, {"name": "D", "weight": 0.7}]},
            {"name": "D", "holdings": [{"name": "C", "weight": 0.5}, {"name": "E", "weight": 0.5}]},
        ]
        exp = {
            "A": 1,
            "B": 0.2,
            "C": 0.93,
            "D": 0.14,
            "E": 0.07,
        }
        _graph = convert_jsonl_to_graph_format(graph)
        ret_val = {}
        # TODO: Fix state caching in recursive function, between runs.
        # ie. avoid having to explicitly reset all inputs!
        dfs(_graph, "A", decimals=2, multiplier=1, ret_val=ret_val)
        assert ret_val == exp


    def test_depth_first_search_real_data(self):
        """Test DFS on the real data."""
        exp = {
            "Ethical Global Fund": 1,
            "Fund B": 0.2,
            "Fund C": 0.5,
            "Fund D": 0.35,
            "Fund E": 0.035,
            "MicroFit": 0.1,
            "GreenCo": 0.06,
            "GrapeCo": 0.347,
            "SolarCorp": 0.028,
            "SpaceY": 0.105,
            "BeanzRUS": 0.21,
            "GoldenGadgets": 0.15,
        }
        _graph = convert_jsonl_to_graph_format(DATA)
        ret_val = {}
        # TODO: Fix state caching in recursive function, between runs.
        # ie. avoid having to explicitly reset all inputs!
        dfs(_graph, "Ethical Global Fund", multiplier=1, ret_val=ret_val)
        assert ret_val == exp
