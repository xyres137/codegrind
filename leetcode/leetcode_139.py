from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    l = 0
    r = 1

    words = []
    d = set(word_dict)
    failed = set()

    while r < len(s) + 1:
        w = s[l:r]
        if w in d and (l, r, w) not in failed:
            words.append((l, r, w))
            l = r
            r = l + 1
        else:
            r += 1

        if l == len(s):
            return True

        if r == len(s) + 1:
            if not words:
                return False

            l, r, w = words.pop()
            failed.add((l, r, w))

    return False
