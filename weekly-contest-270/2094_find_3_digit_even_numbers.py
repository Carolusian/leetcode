# 2094. Finding 3-Digit Even Numbers

# Solution: remove duplicate before hand to avoid TLE

# See: https://leetcode.com/contest/weekly-contest-270/problems/finding-3-digit-even-numbers/

# User Accepted:3442
# User Tried:4171
# Total Accepted:3513
# Total Submissions:8443
# Difficulty:Easy
# You are given an integer array digits, where each element is a digit. The array may contain duplicates.
#
# You need to find all the unique integers that follow the given requirements:
#
# The integer consists of the concatenation of three elements from digits in any arbitrary order.
# The integer does not have leading zeros.
# The integer is even.
# For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.
#
# Return a sorted array of the unique integers.
#
#
#
# Example 1:
#
# Input: digits = [2,1,3,0]
# Output: [102,120,130,132,210,230,302,310,312,320]
# Explanation:
# All the possible integers that follow the rquirements are in the output array.
# Notice that there are no odd integers or integers with leading zeros.
# Example 2:
#
# Input: digits = [2,2,8,8,2]
# Output: [222,228,282,288,822,828,882]
# Explanation:
# The same digit can be used as many times as it appears in digits.
# In this example, the digit 8 is used twice each time in 288, 828, and 882.
# Example 3:
#
# Input: digits = [3,7,5]
# Output: []
# Explanation:
# No even integers can be formed using the given digits.
# Example 4:
#
# Input: digits = [0,2,0,0]
# Output: [200]
# Explanation:
# The only valid integer that can be formed with three digits and no leading zeros is 200.
# Example 5:
#
# Input: digits = [0,0,0]
# Output: []
# Explanation:
# All the integers that can be formed have leading zeros. Thus, there are no valid integers.
#
#
# Constraints:
#
# 3 <= digits.length <= 100
# 0 <= digits[i] <= 9e

import itertools
from typing import List


def three_digits_even():
    """get all 3 digits even numbers"""

    def get_tuple(num):
        return tuple(int(i) for i in str(num))

    return dict((get_tuple(i), i) for i in range(100, 1000) if i & 1 == 0)


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        all_nums = three_digits_even()
        perm = set(itertools.permutations(digits, 3))

        for p in perm:
            if p in all_nums.keys() and all_nums[p] not in res:
                res.append(all_nums[p])
        return sorted(res)
