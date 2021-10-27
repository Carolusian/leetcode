# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
import unittest
import itertools

"""
Solution:
[1, 2, 3]  [7, 4, 1]
[4, 5, 6]=>[8, 5, 2]
[7, 8, 9]  [9, 6, 3]

If see the above, it is just reverse the rows, and then zip the elements in each list: 

[1, 2, 3]  [7, 8, 9]  [7, 4, 1]
[4, 5, 6]=>[4, 5, 6]=>[8, 5, 2]
[7, 8, 9]  [1, 2, 3]  [9, 6, 3]

So `zip(*m[::-1])` shall work, but this is not inplace

If move the elements, in each layer: N = (3/2) = 1

replace by steps when j = 0
0, 0: N - 1 - j => 3 - 1 - 0 => 2, 0

replace by steps when j = 1
0, 1: N - 1 - j => 3 - 1 - 1 => 1, 1 
"""

"""
In-place solution: 
- think the matrix as onion layers
- for a 4x4 matrix, has two layers (4/2), then rotate the edges in each layer
- the number of layers, is floor(N / 2). 
- the a nested for loop to loop through layers, then the elements in the layers
- time: O(NxN) 
- space: 1
"""


def rotate_matrix(m: list[list[int]]) -> list[list[int]]:
    rotated = zip(*m[::-1])
    return [list(r) for r in rotated]


def rotate_matrix_inplace(m: list[list[int]]) -> list[list[int]]:
    # layers/cycles of the matrix onion
    N, inner_levels = len(m), len(m) // 2
    for i in range(0, inner_levels):
        for j in range(i, N - i - 1):
            tmp = m[i][j]
            m[i][j] = m[N - 1 - j][i]
            m[N - 1 - j][i] = m[N - 1 - i][N - 1 - j]
            m[N - 1 - i][N - 1 - j] = m[j][N - 1 - i]
            m[j][N - 1 - i] = tmp

    return m


test_cases = (
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
)
test_funcs = (rotate_matrix, rotate_matrix_inplace)


class Test(unittest.TestCase):
    def test_rotate_matrix(self):
        for test_case in test_cases:
            m, expect = test_case
            for func in test_funcs:
                assert func(m) == expect, f"not equal to expected: {expect}"


if __name__ == "__main__":
    unittest.main()
