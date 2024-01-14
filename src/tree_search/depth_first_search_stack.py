"""Depth First Search via a stack."""

def dfs(graph: dict, node: str) -> dict[str, float]:
    """Depth First Search via a stack, which returns all nodes instead
    of a list of _"first-seen"_ eg.

           A
         .2 .8
        B     C
      .3 .7
     C     D
         .5 .5
        C     E

    - Expect: ["A", "C", "B", "D", "E", "C", "C"].
    - A stack-based DFS with memory: ["A", "C", "B", "D", "E"].

    The code totals the weights for each respective node, as it
    searches down each branch. The same multiplier will be used for
    all neighbouring nodes.

    :param dict graph: Dict of graph keys and sub lists.
    :param str node: Root node to start searching from.
    :returns: dict of Nodes with cumulative weights as values. eg.
        {"A": 1, "B": 0.2, "C": 0.93, "D": 0.14, "E": 0.07,}.
    """
    ret_val = {}
    multiplier = 1
    s = []
    s.append((node, multiplier))
    while s:
        _node, _multiplier = s.pop()

        if _node not in ret_val:
            ret_val[_node] = _multiplier
        else:
            # NOTE: `ret_val[_node] += _multiplier` is _more concise,
            # but it doesn't keep the float constrained to 2 decimal
            # places.
            ret_val[_node] = float(f"{ret_val[_node] + _multiplier:.2f}")

        for node in graph.get(_node, []):
            s.append(
                (node["name"], float(f"{node["weight"] * _multiplier:.2f}"))
            )
    return ret_val
