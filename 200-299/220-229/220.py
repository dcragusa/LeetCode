"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
],  Output: 4

Example 2:
Input: matrix = [
    ['0', '1'],
    ['1', '0']
],  Output: 1

Example 3:
Input: matrix = [['0']]
Output: 0
"""

"""
We solve this using DP. We re-use the input matrix to save space, and iterate across the matrix left to right and top
to bottom. We first convert the string 1s and 0s to integers. Then we realise that for a cell to be part of a square
larger than size 2, its top, left, and top-left neighbours must all be 1s. We thus take the minimum of all the cells
and add 1 if the current cell is a 1. We we iterate we keep track of the current maximum size, then simply square it
at the end to obtain the maximum area.
"""


def maximal_square(matrix):
    num_rows, num_cols = len(matrix), len(matrix[0])
    dp = matrix

    maximum_size = 0
    for row in range(num_rows):
        for col in range(num_cols):
            dp[row][col] = int(matrix[row][col])
            if row and col and matrix[row][col]:
                dp[row][col] = min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1]) + 1
            maximum_size = max(maximum_size, dp[row][col])

    return maximum_size ** 2


assert maximal_square([
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0'],
]) == 4
assert maximal_square([
    ['0', '1'],
    ['1', '0'],
]) == 1
assert maximal_square([['1']]) == 1
assert maximal_square([['0']]) == 0
assert maximal_square([
    ['1', '1', '1', '0', '0'],
    ['1', '1', '1', '0', '0'],
    ['1', '1', '1', '1', '1'],
    ['0', '1', '1', '1', '1'],
    ['0', '1', '1', '1', '1'],
    ['0', '1', '1', '1', '1'],
]) == 16
assert maximal_square([
    ['0', '1', '1', '0', '1'],
    ['1', '1', '0', '1', '0'],
    ['0', '1', '1', '1', '0'],
    ['1', '1', '1', '1', '0'],
    ['1', '1', '1', '1', '1'],
    ['0', '0', '0', '0', '0'],
]) == 9
