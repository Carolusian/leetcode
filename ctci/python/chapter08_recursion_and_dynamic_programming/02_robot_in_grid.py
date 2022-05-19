# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.
# Hints: #152, #178, #217, #237, #262, #359

# keywords: recursion, dp

# Solution: first can work through on paper the cases without obstacle(rock) in the path
# for the following cases [[0, 0], [0, 0]], [[0, 0, 0], [0, 0, 0]], [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
# Then for 2x2, it will be 2, cnt[1][1] + cnt[1][1]
# for 2x3, it will be 3, cnt[1][2] + (cnt[1,2] + cnt[1,2])
# for 3x3, it will be 6, 3 + 2 + 1

# See:
# - https://leetcode.com/problems/unique-paths-ii/


import unittest
from typing import List


def robot_in_grid(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = {}

    def fn(grid, r, c):
        key = (r, c)
        if key in dp:
            return dp[key]

        if r >= m or c >= n or grid[r][c] == 1:
            return 0

        if r == m - 1 and c == n - 1:
            return 1

        dp[key] = fn(grid, r + 1, c) + fn(grid, r, c + 1)
        return dp[key]

    return fn(grid, 0, 0)


test_cases = (
    ([[0, 0], [0, 0]], 2),
    ([[0, 0, 0], [0, 0, 0]], 3),
    ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 6),
    ([[0, 1], [0, 0]], 1),
    ([[0, 0, 0], [0, 1, 0]], 1),
)


class Test(unittest.TestCase):
    def test_robot_in_grid(self):
        for tc in test_cases:
            grid, expect = tc
            self.assertEqual(robot_in_grid(grid), expect)


if __name__ == "__main__":
    unittest.main()
