from typing import List, Dict, Set


# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.


def get_consecutive_subsequences(nums: List[int]) -> Dict[int, int]:
    bases = {}
    peaks = {}

    processed = set()

    for num in nums:
        if num in processed:
            continue

        processed.add(num)

        # Consider adding it as a peak.
        if num - 1 in peaks.keys():
            # num - 1 is a peak, and peaks[num - 1] is the corresponding base
            b = peaks[num - 1]
            bases[b] = num
            peaks[num] = b

            del peaks[num - 1]

            # Maybe merge.
            if num + 1 in bases.keys():
                bases[peaks[num]] = bases[num + 1]
                peaks[bases[num + 1]] = peaks[num]

                del bases[num + 1]

        elif num + 1 in bases.keys():
            # num + 1 is a base. bases[num + 1] is the corresponding peak
            p = bases[num + 1]
            bases[num] = p
            peaks[p] = num

            del bases[num + 1]

        # Else add it as base/peak.
        else:
            bases[num] = num
            peaks[num] = num

    return bases


def get_max_consecutive(subsequences: Dict[int, int]) -> int:
    if not subsequences:
        return 0

    return max(v - k + 1 for k, v in subsequences.items())
