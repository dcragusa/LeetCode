"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1, 2, 3, 4, 5, 6, 7],  k = 3,  Output: [5, 6, 7, 1, 2, 3, 4]
Explanation:
rotate 1 steps to the right: [7, 1, 2, 3, 4, 5, 6]
rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5]
rotate 3 steps to the right: [5, 6, 7, 1, 2, 3, 4]

Example 2:
Input: nums = [-1, -100, 3, 99],  k = 2,  Output: [3, 99, -1, -100]
Explanation:
rotate 1 steps to the right: [99, -1, -100, 3]
rotate 2 steps to the right: [3, 99, -1, -100]
"""

"""
Our first instinct might be to repeatedly pop items from the end of the list and insert them at the front, but this is
horrendously inefficient as inserts to the front are O(n) due to having to move the rest of the list in memory. Much 
better is identifying the front part of the list, extending the list with a copy of that part, then deleting the entire
front part in one operation.
"""


# def rotate(nums, k):
#     k %= len(nums)
#     for _ in range(k):
#         nums.insert(0, nums.pop())


def rotate(nums, k):
    k = (len(nums) - k) % len(nums)
    nums.extend(nums[:k])
    del nums[:k]


nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, 3)
assert nums == [5, 6, 7, 1, 2, 3, 4]

nums = [-1, -100, 3, 99]
rotate(nums, 2)
assert nums == [3, 99, -1, -100]

nums = [1, 2]
rotate(nums, 3)
assert nums == [2, 1]
