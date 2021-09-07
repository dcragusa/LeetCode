"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:
Input: [['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0']]
Output: 6
"""

"""
We base our solution on problem 84, which finds the maximal area of a rectangle. Here we simply add an additional step
which is to sum the columns down to get the column heights for each row, at which point we can utilise problem 84 on
each row to find the max rectangle area over the whole matrix.
"""


from itertools import product


def maximal_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    for col_idx, row_idx in product(range(len(matrix[0])), range(len(matrix))):
        addition = matrix[row_idx-1][col_idx] if row_idx else 0
        matrix[row_idx][col_idx] = int(matrix[row_idx][col_idx]) * (addition + 1)

    max_rect_size = 0
    for row in matrix:
        row.append(0)
        stack = [-1]
        for idx, val in enumerate(row):
            while val < row[stack[-1]]:
                height = row[stack.pop()]
                width = idx - 1 - stack[-1]
                max_rect_size = max(max_rect_size, height * width)
            stack.append(idx)

    return max_rect_size


assert maximal_rectangle([['0', '1']]) == 1

assert maximal_rectangle([['1', '0', '1', '0', '0'],
                          ['1', '0', '1', '1', '1'],
                          ['1', '1', '1', '1', '1'],
                          ['1', '0', '0', '1', '0']]) == 6

assert maximal_rectangle([['1', '0', '1', '0', '1', '1', '1', '0'],
                          ['1', '1', '0', '1', '1', '0', '0', '0'],
                          ['1', '1', '1', '0', '0', '1', '0', '1'],
                          ['1', '0', '1', '1', '1', '1', '1', '0'],
                          ['0', '0', '0', '1', '1', '1', '1', '0']]) == 8

assert maximal_rectangle([['1', '1', '1', '1', '1', '1', '1', '1'],
                          ['1', '1', '1', '1', '1', '1', '1', '0'],
                          ['1', '1', '1', '1', '1', '1', '1', '0'],
                          ['1', '1', '1', '1', '1', '0', '0', '0'],
                          ['0', '1', '1', '1', '1', '0', '0', '0']]) == 21

assert maximal_rectangle([['0', '1', '1', '0', '0', '1', '0', '1', '0', '1'],
                          ['0', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                          ['1', '0', '0', '0', '0', '1', '0', '1', '1', '0'],
                          ['0', '1', '1', '1', '1', '1', '1', '0', '1', '0'],
                          ['0', '0', '1', '1', '1', '1', '1', '1', '1', '0'],
                          ['1', '1', '0', '1', '0', '1', '1', '1', '1', '0'],
                          ['0', '0', '0', '1', '1', '0', '0', '0', '1', '0'],
                          ['1', '1', '0', '1', '1', '0', '0', '1', '1', '1'],
                          ['0', '1', '0', '1', '1', '0', '1', '0', '1', '1']]) == 10
