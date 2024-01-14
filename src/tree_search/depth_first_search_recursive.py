"""Depth First Search via Recursion."""

def dfs(
        graph: dict,
        parent_node: str,
        decimals: int = 3,
        multiplier: int = 1,
        ret_val: dict[str, float] = {},
) -> dict[str, float]:
    """Depth First Search via a recursion, which returns all nodes
    instead of a list of _"first-seen"_ eg.

           A
         .2 .8
        B     C
      .3 .7
     C     D
         .5 .5
        C     E

    - Expect: ["A", "B", "C", "D", "C", "E", "C"].
    - A stack-based DFS with memory: ["A", "B", "C", "D", "E"].

    The code totals the weights for each respective node, as it
    searches down each branch. The same multiplier will be used for
    all neighbouring nodes.

    :param dict graph: Dict of graph keys and sub lists.
    :param str node: Root node to start searching from.
    :param int decimals: Round to X decimal places.
    :returns: dict of Nodes with cumulative weights as values. eg.
        {"A": 1, "B": 0.2, "C": 0.93, "D": 0.14, "E": 0.07,}.
    """
    print(ret_val)
    if parent_node not in ret_val:
        ret_val[parent_node] = multiplier
    else:
        ret_val[parent_node] = (
            float(f"{ret_val[parent_node] + multiplier:.{decimals}f}")
        )

    for node in graph.get(parent_node, []):
        dfs(
            graph,
            node["name"],
            multiplier=float(f'{node["weight"] * multiplier:{decimals}f}'),
            ret_val=ret_val,
        )
    return ret_val


def convert_jsonl_to_graph_format(graph: list) -> dict[str, list]:
    # TODO: Refactor this out to a common function.
    if not isinstance(graph, list):
        return graph
    return {x["name"]: x["holdings"] for x in graph}
