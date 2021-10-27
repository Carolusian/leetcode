# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
# Hints:#17, #74, #702
#
# LeetCode Q73: https://leetcode.com/problems/set-matrix-zeroes/
# ---
# Solution: strict forward. just keep track of the unique row / column index which contains 0
# Big O: O(n^2)

import unittest


def zero_matrix(mat: list[list[int]]) -> list[list[int]]: # keep track of rows and cols containing zeros
    rows, cols = set(), set()
    for i, row in enumerate(mat):
        for j, cell in enumerate(row):
            if cell == 0:
                rows.add(i)
                cols.add(j)

    for i, _ in enumerate(mat):
        for j, _ in enumerate(mat[i]):
            if i in rows or j in cols:
                mat[i][j] = 0

    return mat


test_cases = (
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    (
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
    ),
)


class Test(unittest.TestCase):
    def test_zero_matrix(self):
        for test_case in test_cases:
            mat, expect = test_case
            assert zero_matrix(mat) == expect


if __name__ == "__main__":
    unittest.main()
