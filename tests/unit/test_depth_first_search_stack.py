"""Tests for a Depth First Search Solution via a stack."""
from src.tree_search.depth_first_search_stack import dfs


class TestDepthFirstSearchStack:
    def test_depth_first_search_simple_graph(self):
        """Initial test to do DFS on an arbitrary graph."""
        graph = {
            "A": ["B", "C"],
            "B": ["C", "D"],
            "D": ["C", "E"],
        }
        exp = ["A", "C", "B", "D", "E", "C", "C"]
        assert dfs(graph, "A") == exp
