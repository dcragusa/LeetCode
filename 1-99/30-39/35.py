"""
Given a sorted array and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order. You may assume no duplicates in the array.

Example 1:
Input: [1, 3, 5, 6], 5,  Output: 2

Example 2:
Input: [1, 3, 5, 6], 2,  Output: 1

Example 3:
Input: [1, 3, 5, 6], 7,  Output: 4

Example 4:
Input: [1, 3, 5, 6], 0,  Output: 0
"""

"""
This is trivial with Python's bisect_left. Written out for clarity.
"""

# from bisect import bisect_left
#
#
# def search_insert(nums, target):
#     return bisect_left(nums, target)


def search_insert(nums, target):
    low, high = 0, len(nums)
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


assert search_insert([1, 3, 5, 6], 5) == 2
assert search_insert([1, 3, 5, 6], 2) == 1
assert search_insert([1, 3, 5, 6], 7) == 4
assert search_insert([1, 3, 5, 6], 0) == 0
