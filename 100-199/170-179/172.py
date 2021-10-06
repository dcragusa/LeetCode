"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: n = 3,  Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5,  Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0,  Output: 0
"""

"""
This is fairly simple once we realise the 'trick' to it. Trailing zeros can only be obtained by multiples of 10 in the
factorial - and anything that multiplies to 10 itself, such as 5s and 2s. There will always be a multiple of 2 for each
multiple of 5 we consider, so really we just have to count the multiples of 5. We then have to take care of powers of
5: 25 is 5 x 5, but itself multiples to a power of 10 (25 x 2 = 50), and the same for 125, 625 etc.
What this means in algorithmic terms is simply repeatedly dividing by 5 and adding the truncated result to a total
which we return, when n is less than 5 (as no further 0s will be added).
"""


def trailing_zeros(n):
    total = 0
    while n >= 5:
        n //= 5
        total += n
    return total


assert trailing_zeros(3) == 0
assert trailing_zeros(5) == 1
assert trailing_zeros(0) == 0
assert trailing_zeros(25) == 6
