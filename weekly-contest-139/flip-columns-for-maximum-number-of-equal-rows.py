"""
1072. Flip Columns For Maximum Number of Equal Rows

Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every cell in that column.  Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

Return the maximum number of rows that have all values equal after some number of flips.


Example 1:

Input: [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
Example 2:

Input: [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
Example 3:

Input: [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.


Note:

1 <= matrix.length <= 300
1 <= matrix[i].length <= 300
All matrix[i].length's are equal
matrix[i][j] is 0 or 1
"""


def maxEqualRowsAfterFlips(matrix) -> int:
    def flip(val):
        return 1 - val

    def flip_row(row):
        return [flip(i) for i in row]

    def is_values_equal(row):
        return sum(row) in [0, len(row)]

    def max_rows_of_equal_values(matrix):
        n = 0
        for i, _ in enumerate(matrix):
            if is_values_equal(matrix[i]):
                n += 1
        return n

    # loop through each column
    # then, loop each cell in the column
    # max_rows = max_rows_of_equal_values(matrix)
    # for j, _ in enumerate(matrix[0]):
    #     for i, _ in enumerate(matrix):
    #         matrix[i][j] = flip(matrix[i][j])
    #     temp = max_rows_of_equal_values(matrix)
    #     if temp > max_rows:
    #         max_rows = temp

    # return max_rows

    # find how many rows are equal or equal after being fliped
    # loop each row
    max_rows, i = 1, 0
    while i < len(matrix) - 1:
        n = 1
        j = i + 1
        while j < len(matrix):
            if matrix[i] == matrix[j]:
                n += 1
            elif matrix[i] == flip_row(matrix[j]):
                n += 1
            j += 1
        if n > max_rows:
            max_rows = n
        i += 1
    return max_rows


if __name__ == '__main__':
    # print(maxEqualRowsAfterFlips([[0, 1], [1, 1]]))
    # print(maxEqualRowsAfterFlips([[0, 1], [1, 0]]))
    # print(maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]))
    print(maxEqualRowsAfterFlips([[1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
                                  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                                  [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
                                  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                                  [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]]))
