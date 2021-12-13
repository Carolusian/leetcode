# 2104. Sum of Subarray Ranges
# Keywords: increasing stack

# Solution: increasing stack is useful in find min values of sub-arrays
#
# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
#
# Return the sum of all subarray ranges of nums.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
# See: https://leetcode.com/contest/weekly-contest-271/problems/sum-of-subarray-ranges/


from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """call min and max of the sub-list will cause TLE

        so we keep track of min and max, and use them to find the next min and max values
        """
        ret = 0
        for i, _ in enumerate(nums):
            ma, mi = nums[i], nums[i]
            for j, _ in enumerate(nums[i:]):
                ma = max(ma, nums[i + j])
                mi = min(mi, nums[i + j])
                ret += ma - mi

        return ret

    def subArrayRangesUsingStack(self, nums: List[int]) -> int:
        """
        See: https://leetcode.com/problems/online-stock-span/discuss/168311/

        This post also includes a list of good stack problems
        better explanation: https://www.geeksforgeeks.org/sum-of-minimum-elements-of-all-subarrays/
        """
        pass
