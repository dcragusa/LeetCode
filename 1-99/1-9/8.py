"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is
found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no
effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values,
INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

Example 1:
Input: "42", Output: 42

Example 2:
Input: "   -42", Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words", Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987", Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332", Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−2^31) is returned.
"""

"""
First we strip any whitespace and make a set of number characters for O(1) lookups. If the first character is a +/-,
we start counting from the second character. If any character after this point is not a number, stop counting.
Finally, convert the obtained string into an integer, respecting the - sign if found and the signed int ranges.
"""


def atoi(s):
    s = s.lstrip()
    if not s:
        return 0

    nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    num_str = ''
    negative = False
    idx = 0

    if s[0] == '-':
        negative = True
        idx = 1
    elif s[0] == '+':
        idx = 1

    for char in s[idx:]:
        if char not in nums:
            break
        num_str += char

    if not num_str:
        return 0

    num = -int(num_str) if negative else int(num_str)
    if num < -2**31:
        return -2**31
    elif num >= 2**31:
        return 2**31 - 1
    else:
        return num


assert atoi("42") == 42
assert atoi("   -42") == -42
assert atoi("4193 with words") == 4193
assert atoi("words and 987") == 0
assert atoi("-91283472332") == -2147483648
assert atoi("-") == 0
assert atoi("") == 0
