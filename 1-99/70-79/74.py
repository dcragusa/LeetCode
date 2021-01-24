"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [[1,  3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]]
target = 3,  Output: true

Example 2:
Input:
matrix = [[1,  3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]]
target = 13,  Output: false
"""

"""
We base our solution on two binary searches, seeing as the data is sorted. Firstly we do a bisect_right on the first
column of the matrix to find the row above the one our target should lie in. If this idx is 0, the target is smaller 
than the smallest element, and so cannot be found in the array. We then do a bisect_left to find the index where the
target should be inserted. The target is present in the array if the value at this index is the target.
"""


from bisect import bisect_right, bisect_left


def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    first_col = [row[0] for row in matrix]
    row_idx = bisect_right(first_col, target)
    if not row_idx:
        return False
    col_idx = bisect_left(matrix[row_idx-1], target)
    return col_idx != len(matrix[row_idx-1]) and matrix[row_idx-1][col_idx] == target


assert search_matrix([[]], 1) is False

assert search_matrix([[1]], 1) is True

assert search_matrix([[1,  3,  5,  7],
                      [10, 11, 16, 20],
                      [23, 30, 34, 50]], 3) is True

assert search_matrix([[1,  3,  5,  7],
                      [10, 11, 16, 20],
                      [23, 30, 34, 50]], 13) is False
#
assert search_matrix([[1,  3,  5,  7],
                      [10, 11, 16, 20],
                      [23, 30, 34, 50]], 0) is False

assert search_matrix([[1,  3,  5,  7],
                      [10, 11, 16, 20],
                      [23, 30, 34, 50]], 51) is False
