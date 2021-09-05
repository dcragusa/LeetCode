"""
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input:        Output:
[[1,1,1],    [[1,0,1],
 [1,0,1],     [0,0,0],
 [1,1,1]]     [1,0,1]]

Example 2:
Input:         Output:
[[0,1,2,0],   [[0,0,0,0],
 [3,4,5,2],    [0,4,5,0],
 [1,3,1,5]]    [0,3,1,0]]

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

"""
This is a constant space, linear time solution. A sentinel value object() for a flag is created to guarantee uniqueness. 
Two passes are made over the array: in the first pass, the first value of the row or column is set to the flag. 
Because the top left value can refer to either the row or column, a separate variable with the flag for the first
row is created as well. In the second pass, all values with a flag in their row or column are set to 0. Finally, we 
check the first row and column, setting every flag to 0.
"""


from itertools import product


def set_zeroes(matrix):
    num_rows, num_cols = len(matrix), len(matrix[0])
    flag, flag_first_row = object(), False
    for row_idx, col_idx in product(range(num_rows), range(num_cols)):
        if matrix[row_idx][col_idx] == 0:
            if not row_idx:
                flag_first_row = True
            else:
                matrix[row_idx][0] = flag
            matrix[0][col_idx] = flag

    for row_idx, col_idx in product(range(num_rows), range(num_cols)):
        if matrix[row_idx][col_idx] == flag:
            continue
        if (not row_idx and flag_first_row) or (row_idx and (matrix[row_idx][0] == flag or matrix[0][col_idx] == flag)):
            matrix[row_idx][col_idx] = 0

    for col_idx in range(num_cols):
        if matrix[0][col_idx] == flag:
            matrix[0][col_idx] = 0
    for row_idx in range(1, num_rows):
        if matrix[row_idx][0] == flag:
            matrix[row_idx][0] = 0


matrix = [[1, 1, 1],
          [0, 1, 2]]
set_zeroes(matrix)
assert matrix == [[0, 1, 1],
                  [0, 0, 0]]

matrix = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]
set_zeroes(matrix)
assert matrix == [[1, 0, 1],
                  [0, 0, 0],
                  [1, 0, 1]]

matrix = [[0, 1, 2, 0],
          [3, 4, 5, 2],
          [1, 3, 1, 5]]
set_zeroes(matrix)
assert matrix == [[0, 0, 0, 0],
                  [0, 4, 5, 0],
                  [0, 3, 1, 0]]

matrix = [[8, 3, 6, 9, 7, 8, 0, 6],
          [0, 3, 7, 0, 0, 4, 3, 8],
          [5, 3, 6, 7, 1, 6, 2, 6],
          [8, 7, 2, 5, 0, 6, 4, 0],
          [0, 2, 9, 9, 3, 9, 7, 3]]
set_zeroes(matrix)
assert matrix == [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 3, 6, 0, 0, 6, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]]

matrix = [[-4, -26, 6, -7, 0],
          [-8, 6, -8, -6, 0],
          [26, 2, -9, -6, -10]]
set_zeroes(matrix)
assert matrix == [[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [26, 2, -9, -6, 0]]
