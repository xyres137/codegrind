from typing import Set


def get_maximal_substrings(s: str) -> Set[str]:
    if not s:
        return set()

    words = set()
    seen = {}

    i = 0
    start = 0
    word = ""

    while i < len(s):
        if s[i] not in seen or seen[s[i]] < start:
            word += s[i]
            seen[s[i]] = i

            if i == len(s) - 1:
                words.add(word)
        else:
            words.add(word)
            start = seen[s[i]] + 1
            word = s[start:i + 1]
            seen[s[i]] = i

        i += 1

    return words


def length_of_longest_substring(s: str) -> int:
    substrings = get_maximal_substrings(s)
    if substrings:
        return max(len(s) for s in substrings)
    else:
        return 0
