"""
Given a triangle array, return the minimum path sum from top to bottom. For each step, you may move to an adjacent
number of the row below. More formally, if you are on index i on the current row, you may move to either i or i + 1
on the next row.

Example 1:
Input: triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],  Output: 11
Explanation: The triangle looks like:

     2
    3 4
   6 5 7
  4 1 8 3

The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]],  Output: -10
"""

"""
We can go either top to bottom or bottom to top: the principle is the same. We go row by row, adding each element
to the minimum of the two elements above it (or below, depending on direction). In this way, we are building up a map
of the minimum path at each point. For top to bottom, the minimum path is the lowest number on the bottom row.
For bottom to top, the minimum path is simply the number on the first row.
"""


def minimum_total_top_to_bottom(triangle):
    last_row = triangle[0]
    for row in triangle[1:]:
        for idx, value in enumerate(row):
            if idx == 0:
                addition = last_row[0]
            elif idx == len(row) - 1:
                addition = last_row[-1]
            else:
                addition = min(last_row[idx], last_row[idx - 1])
            row[idx] = value + addition
        last_row = row
    return min(last_row)


def minimum_total_bottom_to_top(triangle):
    last_row = triangle[-1]
    for row in reversed(triangle[:-1]):
        for idx, value in enumerate(row):
            row[idx] = value + min(last_row[idx], last_row[idx + 1])
        last_row = row
    return last_row[0]


assert minimum_total_top_to_bottom([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
assert minimum_total_bottom_to_top([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
assert minimum_total_top_to_bottom([[-10]]) == -10
assert minimum_total_bottom_to_top([[-10]]) == -10
