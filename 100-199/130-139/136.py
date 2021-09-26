"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2, 2, 1],  Output: 1

Example 2:
Input: nums = [4, 1, 2, 1, 2],  Output: 4

Example 3:
Input: nums = [1],  Output: 1
"""

"""
The trick to this is employing bitwise operators. If we know that XOR(a, 0) = a and XOR(a, a) = 0, all we have to
do is XOR every number in nums together. The doubles will cancel each other out, leaving the single number we are 
interested in.
"""


def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


assert single_number([2, 2, 1]) == 1
assert single_number([4, 1, 2, 1, 2]) == 4
assert single_number([1]) == 1
