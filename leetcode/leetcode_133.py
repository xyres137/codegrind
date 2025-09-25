from typing import List, Dict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def _parse_adjacency_list(adj: List[List[int]]) -> Dict[int, Node]:
    g = {i + 1: Node(i + 1) for i in range(len(adj))}

    for i in range(1, len(adj) + 1):
        g[i].neighbors = [g[j] for j in adj[i - 1]]

    return g


def _to_adjacency_list(node: Node) -> List[List[int]]:
    adj_dict = {}

    visited = set()
    stack = [node]

    while stack:
        current = stack.pop()
        if current.val not in visited:
            visited.add(current.val)

            adj_dict[current.val] = [n.val for n in current.neighbors]
            for n in current.neighbors:
                stack.append(n)

    return [adj_dict[i] for i in range(1, len(adj_dict) + 1)]


def clone_with_dfs(marked_node: Node):
    if marked_node is None:
        return {}

    visited = set()
    g = {}
    stack = [marked_node]

    while stack:
        current = stack.pop()
        if current.val not in visited:
            visited.add(current.val)
            if current.val not in g:
                g[current.val] = Node(current.val)

            for neighbor in current.neighbors:
                if neighbor.val not in g:
                    g[neighbor.val] = Node(neighbor.val)

                g[current.val].neighbors.append(g[neighbor.val])
                stack.append(neighbor)

    return g
