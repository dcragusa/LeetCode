"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1, 2, 3, 1], k = 3,  Output: True

Example 2:
Input: nums = [1, 0, 1, 1], k = 1,  Output: True

Example 3:
Input: nums = [1, 2, 3, 1, 2, 3], k = 2,  Output: False
"""

"""
We set up a map of number to index. We iterate through nums - if the number if already in the map, we return True if
the difference in indices is <= k. We then update the number to index map with the current number and index.
"""


def contains_nearby_duplicate(nums, k):
    num_to_idx_map = {}
    for idx, num in enumerate(nums):
        if num in num_to_idx_map and idx - num_to_idx_map[num] <= k:
            return True
        num_to_idx_map[num] = idx
    return False


assert contains_nearby_duplicate([1, 2, 3, 1], 3) is True
assert contains_nearby_duplicate([1, 0, 1, 1], 1) is True
assert contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2) is False
