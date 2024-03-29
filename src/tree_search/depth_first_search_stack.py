"""Depth First Search via a stack."""

def dfs(graph: dict|list, node: str, decimals: int = 3) -> dict[str, float]:
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

    :param dict graph: Dict|list of graph keys and sub lists.
    :param str node: Root node to start searching from.
    :param int decimals: Round to X decimal places.
    :returns: dict of Nodes with cumulative weights as values. eg.
        {"A": 1, "B": 0.2, "C": 0.93, "D": 0.14, "E": 0.07,}.
    """
    ret_val = {}
    _graph = convert_jsonl_to_graph_format(graph)
    multiplier = 1
    s = []
    s.append((node, multiplier))
    while s:
        _node, _multiplier = s.pop()

        if _node not in ret_val:
            ret_val[_node] = _multiplier
        else:
            # NOTE: `ret_val[_node] += _multiplier` is _more concise,
            # but it doesn't keep the float constrained to `decimals`
            # decimal places.
            ret_val[_node] = float(
                f"{ret_val[_node] + _multiplier:.{decimals}f}"
            )

        for node in _graph.get(_node, []):
            s.append(
                (
                    node["name"],
                    float(f"{node["weight"] * _multiplier:.{decimals}f}")
                )
            )
    return ret_val


def convert_jsonl_to_graph_format(graph: list) -> dict[str, list]:
    if not isinstance(graph, list):
        return graph
    return {x["name"]: x["holdings"] for x in graph}
