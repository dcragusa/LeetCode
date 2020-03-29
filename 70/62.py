"""
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point
in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there?

Example 1:
Input: m = 3, n = 2,  Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3,  Output: 28

Constraints:
m >= 1, n <= 100
It is guaranteed that the answer will be less than or equal to 2 * 10^9.
"""

"""
This problem can be reduced to finding the unique permutations of the right and down steps the robot has to take to 
reach the end. An inefficient way to do this would be to calculate every permutation, discarding any duplicates.
Alternatively we can see that the number of permutations of a set is the binomial coefficient n! / (n-k)!, where k is
the length of the set n. The coeffient reduces to n!. The counterpart to the binomial coefficient for multisets is
the multinomial coefficient (n_a + n_b + ... )! / n_a! * n_b! * ... Therefore we just calculate this coefficient.
"""


from math import factorial
from itertools import permutations


def unique_paths_slow(m, n):
    return len(set(permutations([0]*(m-1) + [1]*(n-1))))


def unique_paths_fast(m, n):
    right, down = m - 1, n - 1
    return factorial(right + down) / (factorial(right) * factorial(down))


assert unique_paths_slow(3, 2) == unique_paths_fast(3, 2) == 3
assert unique_paths_slow(3, 3) == unique_paths_fast(3, 3) == 6
assert unique_paths_slow(4, 4) == unique_paths_fast(4, 4) == 20
assert unique_paths_slow(7, 3) == unique_paths_fast(7, 3) == 28

