"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array
nums = [0, 1, 2, 4, 5, 6, 7] might become: [4, 5, 6, 7, 0, 1, 2] if it was rotated 4 times, or [0, 1, 2, 4, 5, 6, 7]
if it was rotated 7 times. Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
[a[n-1], a[0], a[1], a[2], ..., a[n-2]]. Given the sorted rotated array nums they may contain duplicates, return the
minimum element of this array. You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [1, 3, 5],  Output: 1

Example 2:
Input: nums = [2, 2, 2, 0, 1],  Output: 0
"""

"""
This is similar to the difference between problems 81 and 33: duplicates are only a problem if the middle number is 
duplicated. If so, we solve in the same way as 81 and count down from the right side to eliminate duplicates.
"""


def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        while mid < right and nums[mid] == nums[right]:
            right -= 1
        import ipdb; ipdb.set_trace()

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


assert find_min([1, 3, 5]) == 1
assert find_min([2, 2, 2, 0, 1]) == 0
assert find_min([3, 1, 3]) == 1
assert find_min([10, 1, 10, 10, 10]) == 1
