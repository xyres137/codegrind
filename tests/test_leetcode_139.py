from typing import List

from leetcode.leetcode_139 import word_break
import pytest


@pytest.mark.parametrize(
    "s,word_dict,expected",
    [
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("leetcattle", ["leet", "cat", "cattle"], True),
    ],
)
def test_word_break_correctness(s: str, word_dict: List[str], expected: bool):
    assert word_break(s, word_dict) == expected
