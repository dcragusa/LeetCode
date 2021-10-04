"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such
that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where
1 <= first < second <= numbers.length. Return the indices of the two numbers, index1 and index2, as an integer array
[index1, index2] of length 2. The tests are generated such that there is exactly one solution. You may not use the
same element twice.

Example 1:
Input: numbers = [2, 7, 11, 15], target = 9,  Output: [1, 2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2, 3, 4], target = 6,  Output: [1, 3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.

Example 3:
Input: numbers = [-1, 0], target = -1,  Output: [1, 2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2.
"""

"""
Similar to problem 1, except the array is pre-sorted. We can employ the same O(1) time dict-based solution, but if
we want to have an O(1) space based solution, we can take advantage of the sorting to place a pointer at each end of
the numbers array. If the total is less than the target, we know we have to increase the lower pointer, and likewise
we know we have to decrease the upper pointer if the total is greater than the target.
"""


def two_sum_dict(numbers, target):
    index_map = {}
    for idx, num in enumerate(numbers):
        if (diff := target - num) in index_map:
            return [index_map[diff] + 1, idx + 1]
        index_map[num] = idx


def two_sum_pointers(numbers, target):
    low, high = 0, len(numbers) - 1
    while True:
        total = numbers[low] + numbers[high]
        if total == target:
            return [low + 1, high + 1]
        elif total < target:
            low += 1
        elif total > target:
            high -= 1


assert two_sum_dict([2, 7, 11, 15], 9) == two_sum_pointers([2, 7, 11, 15], 9) == [1, 2]
assert two_sum_dict([2, 3, 4], 6) == two_sum_pointers([2, 3, 4], 6) == [1, 3]
assert two_sum_dict([-1, 0], -1) == two_sum_pointers([-1, 0], -1) == [1, 2]
assert two_sum_dict([0, 0, 1, 2], 0) == two_sum_pointers([0, 0, 1, 2], 0) == [1, 2]
assert two_sum_dict([1, 2, 3, 4, 4, 9, 56, 90], 8) == two_sum_pointers([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]
