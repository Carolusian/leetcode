"""
1020. Number of Enclaves

Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
Example 2:

Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.
 

Note:

1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.
"""


def neighbours(A, i, j, existing):
    result = existing
    moves = [
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
    ]
    for m in moves:
        x, y = m 
        if x >= 0 and y >= 0 and x < len(A) and y < len(A[0]) and A[x][y] == 1 and (x, y) not in result:
            result.append((x, y))
            result = neighbours(A, x, y, result)
    
    return result


def numEnclaves(A) -> int:
    existing = []
    d1_boundary = [0, len(A) - 1]
    d2_boundary = [0, len(A[0]) - 1]

    ones = 0
    for i, row in enumerate(A):
        for j, val in enumerate(row):
            if i in d1_boundary or j in d2_boundary:
                if val:
                    existing.append((i, j))
                    existing = neighbours(A, i, j, existing)
            if val == 1:
                ones += 1
    return ones - len(set(existing))


test1 = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
]

test2 = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
]

test3 = [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]

print(numEnclaves(test3))

