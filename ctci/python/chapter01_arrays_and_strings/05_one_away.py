# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# 
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
# 
# Solution: have two cursors traverse both strings, and count the number of edits, if the counter > 1, return False
# if length of two strings are equal, increase in both
# otherwise, increase in the longer string
#
# further readings:
# See also harder version: https://leetcode.com/problems/edit-distance/
# explains in https://en.wikipedia.org/wiki/Edit_distance
# python has difflib: https://codereview.stackexchange.com/questions/217065/calculate-levenshtein-distance-between-two-strings-in-python
# https://blog.paperspace.com/implementing-levenshtein-distance-word-autocomplete-autocorrect/
# solution: https://www.geeksforgeeks.org/edit-distance-dp-5/
# - divide and conquer
# - the top/last case is edit the last character, then recurse the same on substrings
# - the minimum case is compare to empty string
# - Big O is exponential O(3^m): think the generated scenarios as binary tree for O(2^n)

import unittest


def one_away(s1: str, s2: str) -> bool:
    len1, len2 = len(s1), len(s2)
    i, j, edits = 0, 0, 0

    if abs(len1 - len2) > 1:
        return False

    while i < len1 and j < len2:
        if s1[i] == s2[j]:
            i = i + 1
            j = j + 1
        else:
            edits = edits + 1
            if len1 > len2:
                i = i + 1
            elif len1 < len2:
                j = j + 1
            else:
                i = i + 1
                j = j + 1
        if edits > 1:
            return False
    return True


def min_distance(s1: str, s2: str) -> int:
    # recursion approach to calculate the real edit distances from s1 to s2
    # this algorithm will be more general than the one_away function
    # cost: O(3^m) - cannot pass leetcode submission
    len1, len2 = len(s1), len(s2)
    if s1 == s2:
        return 0
    if s1 == "":
        return len2
    if s2 == "":
        return len1

    # consider only edit and delete by swap two variables
    if len1 < len2:
        s1, s2 = s2, s1

    dist = 0 if s1[0] == s2[0] else 1

    # minimum of edited, or deleted s1
    return dist + min(min_distance(s1[1:], s2[1:]), min_distance(s1[1:], s2))


def one_away_recursive(s1: str, s2: str) -> bool:
    return min_distance(s1, s2) <= 1


# TODO: DP solution which could be more efficient


class Test(unittest.TestCase):
    test_cases = (
            ("pale", "ple", True),
            ("pales", "pale", True),
            ("pale", "bale", True),
            ("pale", "bake", False),
            ("pale", "pale12", False),
    )
    test_funcs = (one_away, one_away_recursive)

    def test_one_away(self):
        for test_case in self.test_cases:
            s1, s2, expect = test_case
            for func in self.test_funcs:
                assert func(s1, s2) == expect, f"{func.__name__} failed for {s1} and {s2}"


if __name__ == "__main__":
    # print(min_distance("pale", "pale12"))
    unittest.main()
