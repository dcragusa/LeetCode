"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[[ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Example 2:
Input:
[[1, 2,  3,  4],
 [5, 6,  7,  8],
 [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
"""

"""
We have two approaches: we can keep track of where the borders of our matrix are and iterate concentrically inwards,
decreasing the borders as we process a line, or we can pop the appropriate lists and values off our matrix directly.
The latter is initially much faster but suffers greatly on larger matrices due to the inefficiency of list.pop(0).
"""


def spiral_order(matrix):
    if not matrix or not len(matrix) or not len(matrix[0]):
        return []
    top, bottom, left, right = 0, len(matrix), 0, len(matrix[0])
    results = []

    while True:
        for col in range(left, right):
            results.append(matrix[top][col])
        top += 1
        if left == right:
            return results
        for row in range(top, bottom):
            results.append(matrix[row][right-1])
        right -= 1
        if top == bottom:
            return results
        for col in range(right-1, left-1, -1):
            results.append(matrix[bottom-1][col])
        bottom -= 1
        if left == right:
            return results
        for row in range(bottom-1, top-1, -1):
            results.append(matrix[row][left])
        left += 1
        if top == bottom:
            return results


def spiral_order2(matrix):
    results = []
    if not matrix or not len(matrix) or not len(matrix[0]):
        return results
    while True:
        results.extend(matrix.pop(0))
        if not matrix or not matrix[0]:
            return results
        results.extend([row.pop() for row in matrix])
        if not matrix or not matrix[0]:
            return results
        results.extend(reversed(matrix.pop()))
        if not matrix or not matrix[0]:
            return results
        results.extend(reversed([row.pop(0) for row in matrix]))
        if not matrix or not matrix[0]:
            return results


assert spiral_order([[1, 2, 3]]) == spiral_order2([[1, 2, 3]]) == [1, 2, 3]

assert spiral_order([[1], [2], [3]]) == spiral_order2([[1], [2], [3]]) == [1, 2, 3]

assert spiral_order([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) == spiral_order2([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

assert spiral_order([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]) == spiral_order2([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
