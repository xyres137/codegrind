from typing import List
from leetcode.leetcode_133 import _parse_adjacency_list, _to_adjacency_list, clone_with_dfs

import pytest


@pytest.mark.parametrize(
    "adj_list", [
        [[2, 4], [1, 3], [2, 4], [1, 3]],
        [[]],
        []
    ]
)
def test_clone_has_same_adjacency_list(adj_list: List[List[int]]):
    graph = _parse_adjacency_list(adj_list)
    if graph:
        root_node = graph[1]
        node_clone = clone_with_dfs(root_node)
        clone_adj_list = _to_adjacency_list(node_clone[1])

        assert adj_list == clone_adj_list

