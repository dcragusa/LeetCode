"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array
nums = [0, 1, 2, 4, 5, 6, 7] might become: [4, 5, 6, 7, 0, 1, 2] if it was rotated 4 times, or [0, 1, 2, 4, 5, 6, 7]
if it was rotated 7 times. Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
[a[n-1], a[0], a[1], a[2], ..., a[n-2]]. Given the sorted rotated array nums of unique elements, return the minimum
element of this array. You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3, 4, 5, 1, 2],  Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4, 5, 6, 7, 0, 1, 2],  Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11, 13, 15, 17],  Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
"""

"""
In order to perform with O(log n) time we need to use binary search. We know the array is still going to be in 
scending order, just the minimum can be on either side of the middle. If the middle is lower than the left side, then
we set the left index to be the middle. Otherwise, we set the right side to be the middle. By repeatedly doing this, 
the minimum number will eventually be at the left index.
"""


def find_min(nums):
    left, right = 0, len(nums) - 1
    while nums[left] > nums[right]:
        mid = (left + right) // 2
        if nums[mid] < nums[left]:
            right = mid
        else:
            left = mid + 1
    return nums[left]


assert find_min([4, 5, 1, 2, 3]) == 1
assert find_min([3, 4, 5, 1, 2]) == 1
assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
assert find_min([11, 13, 15, 17]) == 11
