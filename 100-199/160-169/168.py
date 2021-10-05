"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

Example 1:
Input: columnNumber = 1,  Output: 'A'

Example 2:
Input: columnNumber = 28,  Output: 'AB'

Example 3:
Input: columnNumber = 701,  Output: 'ZY'

Example 4:
Input: columnNumber = 2147483647,  Output: 'FXSHRXW'
"""

"""
This is just repeatedly dividing by 26 and appending the results to a string, which we then reverse at the end. We
subtract 1 to obtain the correct letter (as Excel columns are 1-indexed whereas our list of letters is 0-indexed).
"""

from string import ascii_uppercase


def convert_to_title(columnNumber):
    result = ''
    while columnNumber:
        columnNumber -= 1
        columnNumber, remainder = divmod(columnNumber, 26)
        result += ascii_uppercase[remainder]
    return result[::-1]


assert convert_to_title(1) == 'A'
assert convert_to_title(28) == 'AB'
assert convert_to_title(701) == 'ZY'
assert convert_to_title(2147483647) == 'FXSHRXW'
