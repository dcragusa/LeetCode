"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1, 2, 0],  Output: 3

Example 2:
Input: [3, 4, -1, 1],  Output: 2

Example 3:
Input: [7, 8, 9, 11, 12],  Output: 1

Note: Your algorithm should run in O(n) time and uses constant extra space.
"""

"""
We iterate across the array. If the number is between 1 and the length of the array, we move the number to that spot
(-1, because arrays are 0-indexed) and repeat the procedure with the number we are replacing. In this way we get a
sorted array starting at 1 (except negative numbers and numbers beyond the size of the array, which we do not care
about). This makes it trivial to count along the array and return the first missing positive number.
"""


def first_missing_positive(nums):
    for num in nums:
        while 1 <= num <= len(nums) and num != nums[num-1]:
            nums[num-1], num = num, nums[num-1]
    for idx, num in enumerate(nums, start=1):
        if idx != num:
            return idx
    return len(nums) + 1


assert first_missing_positive([0]) == 1
assert first_missing_positive([]) == 1
assert first_missing_positive([1, 2, 0]) == 3
assert first_missing_positive([3, 4, -1, 1]) == 2
assert first_missing_positive([7, 8, 9, 11, 12]) == 1
assert first_missing_positive([3, 1, -2, 4, -1, 0, 2]) == 5
assert first_missing_positive([1, 2]) == 3
assert first_missing_positive([2, 1]) == 3
