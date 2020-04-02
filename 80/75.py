"""
Given an array with n objects colored red, white or blue (represented by integers 0, 1, and 2), sort them in-place so
that objects of the same color are adjacent, with the colors in the order red, white and blue.
Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0],  Output: [0,0,1,1,2,2]

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate over the array counting the number of 0's, 1's, and 2's, then overwrite the array.
Could you come up with a one-pass algorithm using only constant space?
"""

"""
This is a one-pass algorithm with constant space: we iterate over the array, keeping two indices to the front and back
of the array respectively. We make a loop for each element, swapping 0s to the front of the array and 2s to the back,
breaking if we find a 1 or we are moving to the current index. We can stop iterating when we reach the index to the 
back of the array, as we know the rest consists of 2s.
"""


def sort_colors(nums):
    idx, low, high = 0, 0, len(nums) - 1
    while idx <= high:
        while True:
            val = nums[idx]
            if val == 0:
                if idx == low:
                    break
                nums[idx], nums[low] = nums[low], nums[idx]
                low += 1
            elif val == 2:
                if idx == high:
                    break
                nums[idx], nums[high] = nums[high], nums[idx]
                high -= 1
            else:
                break
        idx += 1
    return nums


assert sort_colors([0]) == [0]
assert sort_colors([0, 0]) == [0, 0]
assert sort_colors([0, 1]) == [0, 1]
assert sort_colors([0, 2]) == [0, 2]
assert sort_colors([1, 2]) == [1, 2]
assert sort_colors([2, 1]) == [1, 2]
assert sort_colors([2, 0, 1]) == [0, 1, 2]
assert sort_colors([2, 2, 1, 1, 0, 0]) == [0, 0, 1, 1, 2, 2]
assert sort_colors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
assert sort_colors([1, 2, 2, 2, 2, 0, 0, 0, 1, 1]) == [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
