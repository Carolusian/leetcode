# Power Set: Write a method to return all subsets of a set.
# Hints: #273, #290, #338, #354, #373

# Steps: (1 2 3) for example, P stands for power set function
# P(1 2 3) -> 1 x P(2 3)    [1,2,3] and [1]
# P(2 3) -> 2 x P(3)        [2,3] and [2]
# P(3) -> 3 x P()           [3]
# P() -> ()                 []

# Solution 1: Cascading
# Solution 2: Backtracking
# Solution 3: Lexicographic

# See:
# - https://leetcode.com/problems/subsets/solution/
# - 排列组合的一些公式及推导(非常详细易懂): https://www.cnblogs.com/1024th/p/10623541.html
# - 如何通俗的解释排列公式和组合公式的含义？ - "抓兔子"问题 (兔子自己跳不跳出来): Cn0 + Cn1 + .. + Cnn = 2^n

import unittest
from typing import List


def power_set_cascade(nums: List[int]) -> List[List[int]]:
    """Loop the numbers and then combine with existing result

    O(N * 2^N)

    Sample walkthrough:
    num = 1, ret = [[]]:
     - [] + [1] -> ret
    num = 2, ret = [[], [1]]
     - [2] + [1, 2] -> [[], [1], [2], [1, 2]] -> ret
    num = 3, ret = [[], [1], [2], [1, 2]]
     - [3] + [1,3] + [2,3] + [1, 2, 3] -> [[], [1], [2], [1, 2], [3], [1,3], [2,3], [1, 2, 3]] -> ret
    """
    ret = [[]]
    for num in nums:
        ret += [cur + [num] for cur in ret]
    return ret


def power_set_backtrack(nums: List[int]) -> List[List[int]]:
    """use backtrack (error trialing) technique to get the combination of subsets of all possibility length

    Take len(nums) == 3 for example, all possibility length of the subsets are 0, 1, 2, 3, then we do:

    for k in range(0, 4):
        backtrack()
    """

    def backtrack(first=0, cur=[]):
        print(f"length of subset == {k}, first_index == {first}, cur == {cur}", end=" ")
        if k == len(cur):
            ret.append(cur[:])
            print("appended")
            return
        else:
            print()

        for i in range(first, n):
            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.pop()

    ret = []
    n = len(nums)
    for k in range(0, n + 1):
        backtrack()
        print("====================")
    return ret


test_cases = (
    ([1, 2], [[], [1], [2], [1, 2]]),
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
)


class Test(unittest.TestCase):
    def test_power_set(self):
        for tc in test_cases:
            nums, expect = tc
            self.assertEqual(power_set_cascade(nums), expect)
            self.assertEqual(len(power_set_backtrack(nums)), len(expect))


if __name__ == "__main__":
    unittest.main()
