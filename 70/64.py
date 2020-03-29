"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the
sum of all numbers along its path. Note: You can only move either down or right at any point in time.

Example:
Input: [[1,3,1],
        [1,5,1],
        [4,2,1]]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

"""
We use the same principle as problem 63. The minimum cost to reach a space is the minimum cost of the spaces above
and to the left of it, plus the cost of the space itself. We iterate across the grid, assiging the cost as we go 
in-place. The minimum cost to reach the end will be the last value in the grid.
"""

from itertools import product


def min_path_sum(grid):
    for row_idx, col_idx in product(range(len(grid)), range(len(grid[0]))):
        if row_idx == col_idx == 0:
            continue
        cost_above = float('inf') if not row_idx else grid[row_idx-1][col_idx]
        cost_left = float('inf') if not col_idx else grid[row_idx][col_idx-1]
        grid[row_idx][col_idx] += min(cost_above, cost_left)
    return grid[-1][-1]


assert min_path_sum([[1, 3, 1],
                     [1, 5, 1],
                     [4, 2, 1]]) == 7
