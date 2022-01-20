import collections
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        cnt_ones = sum(1 for num in nums if num == 1)
        nums = nums + nums
        n = len(nums)
        
        running = collections.defaultdict(int)
        if nums[0] == 1: running[0] = 1
        for i in range(1, n):
            if nums[i] == 1: running[i] = running[i - 1] + 1
            else: running[i] = running[i - 1]
        
        
        maxOnes = -2147483648
        # using sliding window
        # technique to find
        # max number of ones in
        # subarray of length x
        for i in range(cnt_ones - 1, n):
            if (i == (cnt_ones - 1)):
                noOfOnes = running[i]
            else:
                noOfOnes = running[i - running[i - cnt_ones]

            if (maxOnes < noOfOnes):
                maxOnes = noOfOnes


        # calculate number of zeros in subarray
        # of length x with maximum number of 1's
        noOfZeroes = cnt_ones - maxOnes

        return noOfZeroes
