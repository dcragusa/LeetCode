"""
Given an integer array nums, return True if any value appears at least twice in the array, and return False if every
element is distinct.

Example 1:
Input: nums = [1, 2, 3, 1],  Output: True

Example 2:
Input: nums = [1, 2, 3, 4],  Output: False

Example 3:
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],  Output: True
"""

"""
Very easy - we take advantage of the fact sets eliminate duplicate elements and compare the length of the list and set.
"""


def contains_duplicate(nums):
    return len(nums) != len(set(nums))


assert contains_duplicate([1, 2, 3, 1]) is True
assert contains_duplicate([1, 2, 3, 4]) is False
assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
