"""
You are climbing a staircase with n steps. Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Example 1:
Input: 2,  Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3,  Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

"""
We can either set up the base cases for 1 and 2 steps, then recur downwards, adding and memoizing as we go.
Alternatively, we can realise that this is the number of unique permutations of a multiset of varying quantities 
of 1s and 2s. For example, for n=6 we must find the unique permutations of the multisets {1, 1, 1, 1, 1, 1}, 
{2, 1, 1, 1, 1}, {2, 2, 1, 1}, and {2, 2, 2}. The number of unique permutations of a multiset is, as we examined in 
problem 62, the multinomial coefficient (n_a + n_b + ... )! / n_a! * n_b! * ... Therefore we just have to calculate 
the multinomial coefficients of the multisets with the number of 2s varying from 0 to n // 2.
"""

from math import factorial
from functools import lru_cache


@lru_cache()
def climb_stairs_slow(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climb_stairs_slow(n-1) + climb_stairs_slow(n-2)


def climb_stairs_fast(n):
    combinations = 1
    twos = 1
    while twos * 2 <= n:
        ones = n - 2*twos
        combinations += factorial(twos + ones) // (factorial(twos) * factorial(ones))
        twos += 1
    return combinations


assert climb_stairs_slow(2) == climb_stairs_fast(2) == 2
assert climb_stairs_slow(3) == climb_stairs_fast(3) == 3
assert climb_stairs_slow(4) == climb_stairs_fast(4) == 5
assert climb_stairs_slow(5) == climb_stairs_fast(5) == 8
assert climb_stairs_slow(6) == climb_stairs_fast(6) == 13
assert climb_stairs_slow(10) == climb_stairs_fast(10) == 89
assert climb_stairs_slow(38) == climb_stairs_fast(38) == 63245986
