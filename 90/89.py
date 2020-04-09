"""
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
A gray code sequence must begin with 0.

Example 1:
Input: 2,  Output: [0,1,3,2]
Explanation: 00 - 0, 01 - 1, 11 - 3, 10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence: 00 - 0, 10 - 2, 11 - 3, 01 - 1

Example 2:
Input: 0,  Output: [0]
Explanation:
We define the gray code sequence to begin with 0. A gray code sequence of n has size = 2^n, which for n = 0 is 2^0 = 1.
Therefore, for n = 0 the gray code sequence is [0].
"""

"""
We implement the algorithm for generating n-bit Gray codes found at https://en.wikipedia.org/wiki/Gray_code.
"""


def gray_code(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    prev_bin = [bin(code)[2:].zfill(n-1) for code in gray_code(n-1)]
    return [int('0'+b, 2) for b in prev_bin] + [int('1'+b, 2) for b in reversed(prev_bin)]


assert gray_code(0) == [0]
assert gray_code(2) == [0, 1, 3, 2]
