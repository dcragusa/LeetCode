"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4,  Output: 2

Example 2:
Input: 8,  Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""

"""
Batteries included with math.sqrt, some alternative implementations are also included from 
https://en.wikipedia.org/wiki/Methods_of_computing_square_roots.
"""

import math


def default_sqrt(x):
    return int(math.sqrt(x))


def babylonian_sqrt(x):
    sq, diff = 1, 1
    while diff > 0.5:
        prev_sq = sq
        sq = ((x / sq) + sq) / 2
        diff = abs(sq - prev_sq)
    return int(sq)


def bakhshali_sqrt(x):
    sq, diff = 1, 1
    while diff > 0.5:
        prev_sq = sq
        a = (x - sq**2) / (2 * sq)
        b = sq + a
        sq = b - a**2 / (2 * b)
        diff = abs(sq - prev_sq)
    return int(sq)


assert default_sqrt(4) == babylonian_sqrt(4) == bakhshali_sqrt(4) == 2
assert default_sqrt(8) == babylonian_sqrt(8) == bakhshali_sqrt(8) == 2
assert default_sqrt(123456789) == babylonian_sqrt(123456789) == bakhshali_sqrt(123456789) == 11111
