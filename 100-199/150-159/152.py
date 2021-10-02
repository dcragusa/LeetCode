"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
and return the product. A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2, 3, -2, 4],  Output: 6
Explanation: [2, 3] has the largest product 6.

Example 2:
Input: nums = [-2, 0, -1],  Output: 0
Explanation: The result cannot be 2, because [-2, -1] is not a subarray.
"""

"""
We implement an algorithm similar to Kadane's (problem 53), but we have to keep track of the local minimum as well, 
since negatives multiplied together form a positive number that could be a maximum.
"""


def max_product(nums):
    global_max = local_max = local_min = nums[0]
    for num in nums[1:]:
        local_max, local_min = max(local_min * num, local_max * num, num), min(local_min * num, local_max * num, num)
        global_max = max(global_max, local_max, local_min)
    return global_max


assert max_product([-2]) == -2
assert max_product([2, 3, -2, 4]) == 6
assert max_product([-2, 0, -1]) == 0
assert max_product([-2, 3, -4]) == 24
assert max_product([-4, -3, -2]) == 12
