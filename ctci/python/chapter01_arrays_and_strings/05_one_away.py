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
# - Big O is exponential O(3^m)

import unittest



def one_away(s1: str, s2: str) -> str:
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
        
        
def min_distance(s1: str, s2: str) -> str:
    # recursion approach to calculate the real edit distances from s1 to s2
    # this algorithm will be more general than the one_away function
    # cost: O(3^m)
    len1, len2 = len(s1), len(s2)
    pass



class Test(unittest.TestCase):
    test_cases = (
            ("pale", "ple", True),
            ("pales", "pale", True),
            ("pale", "bale", True),
            ("pale", "bake", False),
            ("pale", "pale12", False),
    )
    test_funcs = (one_away, min_distance)

    def test_one_away(self):
        for test_case in self.test_cases:
            s1, s2, expect = test_case
            for func in self.test_funcs:
                assert func(s1, s2) == expect, f"{func.__name__} failed for {s1} and {s2}"


if __name__ == "__main__":
    unittest.main()

