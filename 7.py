"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123, Output: 321

Example 2:
Input: -123, Output: -321

Example 3:
Input: 120, Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer
overflows.
"""


def reverse(num):
    negative = True if num < 0 else False
    result = int(str(abs(num))[::-1])
    if negative:
        result = -result
    return result if -2**31 <= result < 2**31 else 0


assert reverse(123) == 321
assert reverse(-123) == -321
assert reverse(120) == 21
