"""
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point
in time. The robot is trying to reach the bottom-right corner of the grid. Now consider if some obstacles are added to
the grids. How many unique paths would there be? An obstacle and empty space is marked as 1 and 0 respectively.

Note: m and n will be at most 100.

Example 1:
Input: [[0,0,0],
        [0,1,0],
        [0,0,0]]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

"""
We can no longer use multinomial coefficients as in problem 62, so we have to calculate paths for each space. We can 
observe that the number of paths to reach a space is equal to the number of paths from the top + number of paths from
the left. We set up an array of equal size to the obstacle grid, filled with 0s. If the start or end space have an 
obstacle in them, we immediately return 0 as there can be no path. Otherwise, we iterate across the obstacle grid and 
assign the current number of paths to num_path depending on whether there is an obstacle above or to the left.
The result is the last value in num_paths.
"""

from itertools import product


def unique_paths_with_obstacles(obstacle_grid):
    num_paths = [[0 for _ in range(len(obstacle_grid[0]))] for _ in range(len(obstacle_grid))]
    if obstacle_grid[0][0] or obstacle_grid[-1][-1]:
        return 0
    num_paths[0][0] = 1
    for row_idx, col_idx in product(range(len(obstacle_grid)), range(len(obstacle_grid[0]))):
        if row_idx == col_idx == 0:
            continue
        paths_above = 0 if not row_idx else (
            0 if obstacle_grid[row_idx-1][col_idx] else num_paths[row_idx-1][col_idx])
        paths_left = 0 if not col_idx else (
            0 if obstacle_grid[row_idx][col_idx-1] else num_paths[row_idx][col_idx-1])
        num_paths[row_idx][col_idx] = paths_above + paths_left
    return num_paths[-1][-1]


assert unique_paths_with_obstacles([[1]]) == 0

assert unique_paths_with_obstacles([[0, 0, 0],
                                    [0, 0, 0]]) == 3

assert unique_paths_with_obstacles([[0, 1, 0],
                                    [0, 1, 0]]) == 0

assert unique_paths_with_obstacles([[0, 0, 0],
                                    [0, 1, 0],
                                    [0, 0, 0]]) == 2

assert unique_paths_with_obstacles([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]]) == 6

assert unique_paths_with_obstacles([[0, 0, 0, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]]) == 20

assert unique_paths_with_obstacles([[0, 0, 0, 1],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0]]) == 19
