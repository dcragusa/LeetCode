"""
A peak element is an element that is strictly greater than its neighbors. Given an integer array nums, find a peak
element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. You may
imagine that nums[-1] = nums[n] = -∞. You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1, 2, 3, 1],  Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1, 2, 1, 3, 5, 6, 4],  Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the
peak element is 6.

Constraints:
nums[i] != nums[i + 1] for all valid i.
"""

"""
To implement an O(log n) time algorithm, we must use binary search. It may not be immediately obvious how to use
binary search, but the clue given is that we may return *any* valid peak - and that there are no consecutive equal
numbers (as, for e.g. in the array [3, 3, 3] no peak would be possible). Hence, we examine the slope of the middle
number by comparing it to the next number. If it is on an ascending slope, we know there must be a peak on the right
side: either there will be a descending number eventually (and thus a peak), or the numbers will ascend until the end
of the array (and thus a peak at the edge). The logic is the same for a descending slope, but on the left side.
"""


def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid
    return left


assert find_peak_element([1, 2, 3, 1]) == 2
assert find_peak_element([1, 2, 1, 3, 5, 6, 4]) == 5
