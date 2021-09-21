"""
Given an integer rowIndex, return the rowIndex'th (0-indexed) row of Pascal's triangle.

Example 1:
Input: rowIndex = 3,  Output: [1, 3, 3, 1]

Example 2:
Input: rowIndex = 0,  Output: [1]

Example 3:
Input: rowIndex = 1,  Output: [1, 1]
"""

"""
Here comes the aforementioned trickery I spoke of in 118... given rowIndex, we know the size of the output row and that
each end consists of 1s. Therefore we can start off by generating a row of 1s. Then, we rely on the fact that to 
generate a 0-based row on its own, we can multiply by successive fractions. So, for e.g. rowIndex = 5, we can multiply
1 by 5/1 to get 5. Then we multiply 5 by 4/2 to get 10. We could continue in the same vein, but exploiting the symmetry 
of the tree is faster. Thus we can construct any row by iterating from the second element to the middle of the row.
"""


def get_row(rowIndex):
    row = [1] * (rowIndex + 1)
    last_number = 1
    for idx in range(1, rowIndex // 2 + 1):
        last_number = (last_number * (rowIndex + 1 - idx)) // idx
        row[idx] = last_number
        row[-idx-1] = last_number
    return row


assert get_row(3) == [1, 3, 3, 1]
assert get_row(0) == [1]
assert get_row(1) == [1, 1]
assert get_row(5) == [1, 5, 10, 10, 5, 1]
