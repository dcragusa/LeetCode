"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous
subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no
such subarray, return 0 instead.

Example 1:
Input: target = 7,  nums = [2, 3, 1, 2, 4, 3],  Output: 2
Explanation: The subarray [4, 3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4,  nums = [1, 4, 4],  Output: 1

Example 3:
Input: target = 11,  nums = [1, 1, 1, 1, 1, 1, 1, 1],  Output: 0
"""

"""
We utilise a two-pointer approach. We initialise the left and right pointers, as well as the array sum, to 0. We also
initialise the min_length to infinity. We increment the array_sum by the value of the right pointer and move the right
pointer up at each step. If the array_sum is bigger than the target, we strip elements from the left side by 
subtracting the value of the left pointer and moving the left pointer up, and update the min_length. We keep doing this
until the array_sum is no longer bigger than the target, then we move the right pointer again. We check to see if there
was a minimum length at all (otherwise, return 0) before returning min_length.
"""


def min_subarray_len(target, nums):
    left = right = array_sum = 0
    min_length = float('inf')
    while right < len(nums):
        array_sum += nums[right]
        right += 1
        while array_sum >= target:
            min_length = min(min_length, right-left)
            array_sum -= nums[left]
            left += 1
    return 0 if min_length == float('inf') else min_length


assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
assert min_subarray_len(4, [1, 4, 4]) == 1
assert min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
