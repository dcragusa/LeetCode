"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3,  Output:[[ 1, 2, 3 ],
                   [ 8, 9, 4 ],
                   [ 7, 6, 5 ]]
"""

"""
First we set up a zero-filled matrix of the appropriate size, then we use similar logic to problem 54, going 
concentrically inwards from the top left. We can use itertools.count to neatly assign increasing values of i as we go,
but we have to use a different method of terminating the loop as the value of a generator is not easily accessible.
"""

from itertools import count


def generate_matrix(n):
    if not n:
        return [[]]
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    top_idx, bottom_idx, left_idx, right_idx = 0, n, 0, n
    up, down, left, right = 1, 2, 3, 4
    direction = right
    i = count(start=1)
    while top_idx <= bottom_idx and left_idx <= right_idx:
        if direction == right:
            for col in range(left_idx, right_idx):
                matrix[top_idx][col] = next(i)
            top_idx += 1
            direction = down
        elif direction == down:
            for row in range(top_idx, bottom_idx):
                matrix[row][right_idx-1] = next(i)
            right_idx -= 1
            direction = left
        elif direction == left:
            for col in range(right_idx-1, left_idx-1, -1):
                matrix[bottom_idx-1][col] = next(i)
            bottom_idx -= 1
            direction = up
        else:
            for row in range(bottom_idx-1, top_idx-1, -1):
                matrix[row][left_idx] = next(i)
            left_idx += 1
            direction = right
    return matrix


assert generate_matrix(0) == [[]]
assert generate_matrix(1) == [[1]]
assert generate_matrix(2) == [[1, 2],
                              [4, 3]]
assert generate_matrix(3) == [[1, 2, 3],
                              [8, 9, 4],
                              [7, 6, 5]]
assert generate_matrix(4) == [[1, 2, 3, 4],
                              [12, 13, 14, 5],
                              [11, 16, 15, 6],
                              [10, 9, 8, 7]]
