# 5907. Next Greater Numerically Balanced Number
# User Accepted:1067
# User Tried:1447
# Total Accepted:1085
# Total Submissions:2582
# Difficulty:Medium
# An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.
#
# Given an integer n, return the smallest numerically balanced number strictly greater than n.
#
#
#
# Example 1:
#
# Input: n = 1
# Output: 22
# Explanation:
# 22 is numerically balanced since:
# - The digit 2 occurs 2 times.
# It is also the smallest numerically balanced number strictly greater than 1.
# Example 2:
#
# Input: n = 1000
# Output: 1333
# Explanation:
# 1333 is numerically balanced since:
# - The digit 1 occurs 1 time.
# - The digit 3 occurs 3 times.
# It is also the smallest numerically balanced number strictly greater than 1000.
# Note that 1022 cannot be the answer because 0 appeared more than 0 times.
# Example 3:
#
# Input: n = 3000
# Output: 3133
# Explanation:
# 3133 is numerically balanced since:
# - The digit 1 occurs 1 time.
# - The digit 3 occurs 3 times.
# It is also the smallest numerically balanced number strictly greater than 3000.
#
#
# Constraints:
#
# 0 <= n <= 106


import unittest
from collections import Counter


def next_beautiful_number(n: int) -> int:
    m = n
    while True:
        m = m + 1
        cnt = Counter(str(m))

        matches = 0
        for k, v in cnt.items():
            if int(k) == v:
                matches = matches + 1

        if matches == len(cnt):
            print(m)
            return m


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        return next_beautiful_number(n)


class Test(unittest.TestCase):
    test_cases = (
        (1000, 1333),
        (1, 22),
        (3000, 3133),
    )

    def test_next_beautiful_number(self):
        for test_case in self.test_cases:
            n, expect = test_case
            assert next_beautiful_number(n) == expect


# next_beautiful_number(1000)
# next_beautiful_number(1)
# next_beautiful_number(3000)
unittest.main()
