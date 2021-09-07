"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

Example:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],  Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.
"""

"""
We implement Kadane's algorithm: https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane%27s_algorithm
"""


def max_subarray(nums):
    if not nums:
        return 0
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


assert max_subarray([]) == 0
assert max_subarray([-2]) == -2
assert max_subarray([-2, -2]) == -2
assert max_subarray([-2, 10, -3]) == 10
assert max_subarray([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]) == 6
assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
