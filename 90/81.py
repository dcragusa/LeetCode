"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0,  Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3,  Output: false

This is a follow up to problem 33. How and why does containing duplicates affect the run-time complexity?
"""

"""
This is not significantly more complex than problem 33: duplicates do not affect the binary search algorithm, unless
the pivot has a duplicate. Then we cannot rely on splitting the list into two halves (greater than and smaller than 
the pivot). In this case, we simply count down from the end of the list until the pivot is no longer duplicated.
Thus in the best case (pivot not duplicated), the performance is equal: O(log n). In the worst case (every element 
except the second is a duplicate of the pivot), the performance is O(n) due to the while loop lowering the high idx.
"""


def search(nums, target):
    if not nums:
        return False
    low, high = 0, len(nums) - 1
    pivot = nums[0]
    while pivot == nums[high]:
        high -= 1
    while low <= high:
        mid = (low + high) // 2
        mid_num = nums[mid]

        if target < pivot <= mid_num:
            mid_num = float('-inf')
        elif mid_num < pivot <= target:
            mid_num = float('inf')

        if target == mid_num:
            return True
        elif target < mid_num:
            high = mid - 1
        else:
            low = mid + 1
    return False


assert search([2, 5, 6, 0, 0, 1, 2], 0) is True
assert search([2, 5, 6, 0, 0, 1, 2], 3) is False
assert search([1, 3, 1, 1, 1], 3) is True
