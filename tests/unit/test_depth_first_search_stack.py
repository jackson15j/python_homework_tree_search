"""Tests for a Depth First Search Solution via a stack."""
from src.tree_search.depth_first_search_stack import dfs


class TestDepthFirstSearchStack:
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
        assert dfs(graph, "A") == exp
