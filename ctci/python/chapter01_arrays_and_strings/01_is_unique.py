import unittest
from collections import defaultdict
from functools import singledispatch
from typing import AnyStr


class Test(unittest.TestCase):
    def test_is_unique(self):
        self.assertEqual(is_unique("abc"), True)
        self.assertEqual(is_unique(b"adfjkdlsfsdjklfhjdklafgeuwoo"), False)
        self.assertEqual(is_unique("adfjkdlsfsdjklfhjdklafgeuwoo"), False)
        self.assertEqual(is_unique(b"adfjkls"), True)


@singledispatch
def is_unique(s: AnyStr) -> bool:
    """If a string has all unique characters"""
    char_set: dict = defaultdict(bool)
    for _, c in enumerate(s):
        if char_set[c]:
            return False
        char_set[c] = True
    return True


@is_unique.register
def _(s: bytes) -> bool:
    """Use bitwise operation to save space, for characters [a-z]"""
    checker = 0
    for _, c in enumerate(s):
        # relative position from 'a'
        val = c - ord('a')
        # if a position has already exist, if yes, return false
        if (checker & (1 << val)) > 0:
            return False
        # mark the position as exist
        # this is the same as operating a dict[int, bool] hashtable
        # where the position represent the ascii code of the character
        # and the bit represent whether it appears before
        checker = checker | (1 << val)
    return True


if __name__ == "__main__":
    unittest.main()
