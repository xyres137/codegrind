from typing import List, Dict, Tuple
from leetcode.leetcode_128 import get_consecutive_subsequences
import random

import pytest

random.seed(42)


def make_shuffled_input(ranges: List[Tuple[int, int]]):
    assembled = []

    for a, b in ranges:
        assembled.extend(range(a, b))
    random.shuffle(assembled)
    return assembled


@pytest.mark.parametrize(
    "input_nums,expected",
    [
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], {0: 8}),
        ([100, 4, 200, 1, 3, 2], {1: 4, 100: 100, 200: 200}),
        ([1, 2, 0, 1], {0: 2}),
        ([0], {0: 0}),
        ([-2, -1, 2, 3], {-2: -1, 2: 3}),
        ([], {}),
        (make_shuffled_input([(0, 50), (100, 200)]), {0: 49, 100: 199}),
        (make_shuffled_input([(0, 50), (40, 200)]), {0: 199}),
    ],
)
def test_correct_subsequences(input_nums: List[int], expected: Dict[int, int]):
    assert get_consecutive_subsequences(input_nums) == expected
