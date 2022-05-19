# 8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.
# Hints: #152, #178, #217, #237, #262, #359

# Keywords: recursion, fibonacci, tribonacci
# Solution 1:
# - traditional recursion and hashmap
# Solution 2:
# - Use a queue to keep track of recursive results

# See:
# - https://leetcode.com/problems/n-th-tribonacci-number/
import unittest
import collections
from unittest.case import TestCase


class Solution:
    def __init__(self):
        self.dp = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        """Traditional recursion + dp"""
        if n < 3:
            return self.dp[n]

        if n in self.dp:
            return self.dp[n]

        self.dp[n] = (
            self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
        )
        return self.dp[n]


class QueueSolution:
    def tribonacci(self, n: int) -> int:
        """Use a queue to keep tracking of previous results"""
        last_three = collections.deque([0, 1, 1])
        if n < 3:
            return last_three[n]

        for _ in range(3, n + 1):
            last_three.append(sum(last_three))
            last_three.popleft()
        return last_three[-1]


test_cases = (
    (4, 4),
    (10, 149),
)


class Test(unittest.TestCase):
    def test_solutions(self):
        for solution_cls in [Solution, QueueSolution]:
            for tc in test_cases:
                n, expect = tc
                sol = solution_cls()
                self.assertEqual(sol.tribonacci(n), expect)


if __name__ == "__main__":
    unittest.main()
