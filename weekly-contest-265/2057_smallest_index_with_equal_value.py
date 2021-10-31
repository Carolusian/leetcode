# 2057. Smallest Index With Equal Value
# User Accepted:5080
# User Tried:5150
# Total Accepted:5157
# Total Submissions:6611
# Difficulty:Easy
# Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.
#
# x mod y denotes the remainder when x is divided by y.
#
#
#
# Example 1:
#
# Input: nums = [0,1,2]
# Output: 0
# Explanation:
# i=0: 0 mod 10 = 0 == nums[0].
# i=1: 1 mod 10 = 1 == nums[1].
# i=2: 2 mod 10 = 2 == nums[2].
# All indices have i mod 10 == nums[i], so we return the smallest index 0.
# Example 2:
# Input: nums = [4,3,2,1]
# Output: 2
# Explanation:
# i=0: 0 mod 10 = 0 != nums[0].
# i=1: 1 mod 10 = 1 != nums[1].
# i=2: 2 mod 10 = 2 == nums[2].
# i=3: 3 mod 10 = 3 != nums[3].
# 2 is the only index which has i mod 10 == nums[i].
# Example 3:
#
# Input: nums = [1,2,3,4,5,6,7,8,9,0]
# Output: -1
# Explanation: No index satisfies i mod 10 == nums[i].
# Example 4:
#
# Input: nums = [2,1,3,5,2]
# Output: 1
# Explanation: 1 is the only index with i mod 10 == nums[i].
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 9

import unittest
from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        res = -1
        for i, n in enumerate(nums):
            if i % 10 == n and (res == -1 or i < res):
                res = i
        return res


test_cases = (
    ([0, 1, 2], 0),
    ([4, 3, 2, 1], 2),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], -1),
    ([2, 1, 3, 5, 2], 1),
)


class Test(unittest.TestCase):
    def test_smallest_index_with_equal_value(self):
        for test_case in test_cases:
            nums, expect = test_case
            solution = Solution()
            self.assertEqual(solution.smallestEqual(nums), expect)


if __name__ == "__main__":
    unittest.main()
