"""
Given an integer numRows, return the first numRows rows of Pascal's triangle.

Example 1:
Input: numRows = 5,  Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

Example 2:
Input: numRows = 1,  Output: [[1]]

Constraints:  1 <= numrows <= 30
"""

"""
We know numRows has to be at least 1, so we can start with the first row = [1]. We could probably do some clever trick 
if only the numRows'th row was required, but seeing as all of them are, we have to iterate. We keep a record of the 
last row, then construct the current row with 1s on the edges and the summation along the last row. Repeat until done.
"""


def generate(numRows):
    rows = [[1]]
    last_row = [1]
    for _ in range(1, numRows):
        current_row = [1] + [last_row[idx] + last_row[idx + 1] for idx in range(0, len(last_row) - 1)] + [1]
        rows.append(current_row)
        last_row = current_row
    return rows


assert generate(1) == [[1]]
assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
