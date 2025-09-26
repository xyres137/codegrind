from typing import List


def find_summands_unordered(arr, start, target_sum):
    possible_targets = set()
    summands = set()
    for i in range(start, len(arr)):
        a = arr[i]
        if a in possible_targets:
            summands.add((a, target_sum - a))
        else:
            possible_targets.add(target_sum - a)
    return summands


def three_sum(nums: List[int]) -> List[List[int]]:
    solutions = set()

    for i in range(len(nums)):
        summands = find_summands_unordered(nums, i + 1, -nums[i])
        for x, y in summands:
            solutions.add(tuple(sorted((nums[i], x, y))))

    return [list(sol) for sol in solutions]
