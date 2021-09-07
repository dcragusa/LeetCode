"""
You are given an n x n 2D matrix representing an image. Rotate the matrix 90 degrees clockwise in-place.

Example 1:
[[1, 2, 3],     [[7, 4, 1],
 [4, 5, 6],  ->  [8, 5, 2],
 [7, 8, 9]],     [9, 6, 3]]

Example 2:
[[ 5,  1,  9, 11],     [[15, 13,  2,  5],
 [ 2,  4,  8, 10],  ->  [14,  3,  4,  1],
 [13,  3,  6,  7],      [12,  6,  8,  9],
 [15, 14, 12, 16]],     [16,  7, 10, 11]]
"""

"""
We work our way through one side of concentrically smaller squares, shifting every side of the square clockwise.
"""


def rotate(matrix):
    n = len(matrix)
    for row_idx in range(n//2):
        for col_idx in range(row_idx, square_size := n-row_idx-1):
            diff = col_idx - row_idx
            top = matrix[row_idx][col_idx]
            matrix[row_idx][col_idx] = matrix[square_size - diff][row_idx]                 # top from left
            matrix[square_size - diff][row_idx] = matrix[square_size][square_size - diff]  # left from bottom
            matrix[square_size][square_size - diff] = matrix[row_idx + diff][square_size]  # bottom from right
            matrix[row_idx + diff][square_size] = top                                      # right from top


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
rotate(matrix)
assert matrix == [[7, 4, 1],
                  [8, 5, 2],
                  [9, 6, 3]]

matrix = [[5,  1,  9,  11],
          [2,  4,  8,  10],
          [13, 3,  6,  7],
          [15, 14, 12, 16]]
rotate(matrix)
assert matrix == [[15, 13, 2, 5],
                  [14, 3, 4, 1],
                  [12, 6, 8, 9],
                  [16, 7, 10, 11]]

matrix = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]
rotate(matrix)
assert matrix == [[21, 16, 11, 6, 1],
                  [22, 17, 12, 7, 2],
                  [23, 18, 13, 8, 3],
                  [24, 19, 14, 9, 4],
                  [25, 20, 15, 10, 5]]
