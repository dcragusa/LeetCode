"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target
value. Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8,  Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6,  Output: [-1,-1]
"""

"""
We use left and right array bisection to find the insertion points of the target. If the target does not exist in the
array, there will be no difference in the insertion points so we return [-1, -1]. Otherwise, we return the left 
bisection result (as it displaces the existing target) and the right bisection result - 1 (as the idx comes after the
last target).
"""

from bisect import bisect_left, bisect_right


def search_range(nums, target):
    start = bisect_left(nums, target)
    end = bisect_right(nums, target, lo=start)
    return [-1, -1] if start == end else [start, end-1]


assert search_range([], 1) == [-1, -1]
assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
