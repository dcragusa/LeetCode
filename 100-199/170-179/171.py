"""
Given a string columnTitle that represents the column title as it appears in an Excel sheet, return its corresponding
column number.

Example 1:
Input: columnTitle = 'A',  Output: 1

Example 2:
Input: columnTitle = 'AB',  Output: 28

Example 3:
Input: columnTitle = 'ZY',  Output: 701

Example 4:
Input: columnTitle = 'FXSHRXW',  Output: 2147483647
"""

"""
The reverse of problem 168 - we iterate backwards through the string, adding powers of 26 to a total as we go.
"""


def title_to_numer(columnTitle):
    total = 0
    for idx, char in enumerate(reversed(columnTitle)):
        total += (26 ** idx) * (ord(char) - 64)
    return total


assert title_to_numer('A') == 1
assert title_to_numer('AB') == 28
assert title_to_numer('ZY') == 701
assert title_to_numer('FXSHRXW') == 2147483647
