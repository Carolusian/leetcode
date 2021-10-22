# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# 
# Solution idea: count the occurrence of the characters, if more than 1 odd characters, then return false

import unittest
from collections import Counter


def palindrome_permutation_set(s: str) -> bool:
    # use set to track if more than 1 characters appear odd times
    container = set()
    for c in s:
        if c in container:
            container.remove(c)
        else:
            container.add(c)
    return len(container) <= 1


def palindrome_permutation_counter(s: str) -> bool:
    # use Counter to keep track of the count of characters
    # keep odd characters, see if the length is <= 1
    ct = Counter(s)
    return len([k for k, v in ct.items() if v % 2 != 0]) <= 1
    

class Test(unittest.TestCase):
    test_cases = (
            ("racecar", True),
            ("rcaerca", True),
            ("racecap", False),
            ("rcaepca", False),
    )
    test_funcs = (palindrome_permutation_set, palindrome_permutation_counter)

    def test_palindrom_permutation(self):
        for test_case in self.test_cases:
            s, expect = test_case
            for func in self.test_funcs:
                assert func(s) == expect, f"{func.__name__} failed for '{s}'"


if __name__ == "__main__":
    unittest.main()
