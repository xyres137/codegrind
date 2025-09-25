# Problem description:
# You get an array of positive integers arr and a positive integer s.
# Find if there exist two numbers a, b in arr, such that s = a + b


from typing import List, Tuple
import bisect


#
# For a first try we assume that the array is sorted.
#


def find_summands(arr: List[int], target_sum: int) -> Tuple[int, int] | None:
    for i in range(len(arr) - 1):
        if arr[i] > target_sum:
            return None

        b = target_sum - arr[i]

        leg = arr[i + 1 :]
        idx = bisect.bisect_left(leg, b)
        if idx < len(leg) and leg[idx] == b:
            return arr[i], b

    return None


#
# Assume now that the array is not sorted, and we don;t want to sort it.
#


def find_summands_unordered(arr: List[int], target_sum: int) -> Tuple[int, int] | None:
    possible_targets = set()

    for a in arr:
        if a < target_sum:
            if a in possible_targets:
                return a, target_sum - a
            else:
                possible_targets.add(target_sum - a)

    return None


a = [1, 2, 4, 4]
print(find_summands_unordered(a, 7))
