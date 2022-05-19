# Power Set: Write a method to return all subsets of a set.
# Hints: #273, #290, #338, #354, #373

import unittest
from typing import List


def power_set(nums: List[int]) -> List[List[int]]:
    def fn(nums):
        pass

    for k, v in enumerate(nums):
        print(v, [v] + nums[:k] + nums[k + 1 :])


class Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    power_set([1, 2, 3])
