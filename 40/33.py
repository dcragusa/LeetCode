"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3, Output: -1
"""

"""
To achieve O(log n) we must perform a binary search, but we cannot do it straightforwardly because of the rotation. 
Let us split the list into two halves, left (all numbers greater than the pivot) and right (all numbers smaller).
We can now perform binary search as usual, as long as we are careful that the mid point and target are in the same
half (otherwise they will not converge). If they are in different halves, we can force the search to go to the other
half by comparing to -inf or inf as appropriate. For the above example 1, we start with our mid at 7 and target at 0. 
The pivot is 4, so we are in different halves. Because the mid is larger than the pivot but the target smaller, we must
force the search into the right half by setting the mid to -inf.
"""


def search(nums, target):
    if not nums:
        return -1
    low, high = 0, len(nums) - 1
    pivot = nums[0]
    while low <= high:
        mid = (low + high) // 2
        mid_num = nums[mid]

        if target < pivot <= mid_num:
            mid_num = float('-inf')
        elif mid_num < pivot <= target:
            mid_num = float('inf')

        if target == mid_num:
            return mid
        elif target < mid_num:
            high = mid - 1
        else:
            low = mid + 1
    return -1


assert search([], 5) == -1
assert search([5], 5) == 0
assert search([1, 3], 0) == -1
assert search([1, 3], 2) == -1
assert search([1, 3], 3) == 1
assert search([5, 1], 5) == 0
assert search([2, 3, 4, 5, 1], 1) == 4
assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 5, 6, 7], 23) == 3
