"""Depth First Search via a stack."""

def dfs(graph: dict, node: str) -> list:
    """Depth First Search via a stack, which returns all nodes instead
    of a list of _"first-seen"_ eg.

           A
         B   C
       C  D
           E

    - Expect: ["A", "C", "B", "D", "E", "C", "C"].
    - A stack-based DFS with memory: ["A", "C", "B", "D", "E"].

    :param dict graph: Dict of graph keys and sub lists.
    :param str node: Root node to start searching from.
    :returns: list of Nodes.
    """
    ret_val = []
    s = []
    s.extend(node)
    while s:
        node = s.pop()
        ret_val.append(node)
        for node in graph.get(node, []):
            s.append(node)
    return ret_val
