"""
Given an array nums of size n, return the majority element. The majority element is the element that appears more
than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3, 2, 3],  Output: 3

Example 2:
Input: nums = [2, 2, 1, 1, 1, 2, 2],  Output: 2
"""

"""
This can be trivially implemented using Counter in O(n) time, but also requires O(n) space to store the count map. For
an O(n) time, O(1) space algorithm, we can turn to the Boyer-Moore majority vote algorithm. This consists of setting
up two variables, majority and count initialised to 0. We then iterate across the nums array. If count is 0, set that
number to be the majority. Otherwise, add 1 to count if the number is the majority, and subtract 1 if it isn't.
For an intuitive understanding, we can realise that when count reaches 0, we are effectively discarding the entire
part of nums up to that point. Since we cannot discard more majority than minority elements, we are always guaranteed
to find the majority in any remaining part of the array. This can continue until we reach the end of the array with a
positive count (in which case the majority is obvious), or the majority will be the last element by default.
Important to note is that this only works because we are guaranteed to have a majority element present - Boyer-Moore
does not work otherwise.
"""

from collections import Counter


def majority_element_counter(nums):
    return Counter(nums).most_common(1)[0][0]


def majority_element_boyer_moore(nums):
    majority, count = None, 0
    for num in nums:
        if not count:
            majority, count = num, 1
        elif num == majority:
            count += 1
        else:
            count -= 1
    return majority


assert majority_element_counter([3, 2, 3]) == majority_element_boyer_moore([3, 2, 3]) == 3
assert majority_element_counter([2, 2, 1, 1, 1, 2, 2]) == majority_element_boyer_moore([2, 2, 1, 1, 1, 2, 2]) == 2
