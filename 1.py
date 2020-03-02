"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

"""
We build up a dict of numbers we have already seen, so lookups are O(1). 
This way we can complete the problem in one pass.
"""


# def two_sum_brute(nums, target):
#     for idx, num in enumerate(nums):
#         temp_target = target - num
#         for other_idx, other_num in enumerate(nums[idx+1:], start=idx+1):
#             if other_num == temp_target:
#                 return [idx, other_idx]


def two_sum_dict(nums, target):
    idxs_of_nums_seen = {}
    for idx, num in enumerate(nums):
        if (other_num := target - num) in idxs_of_nums_seen:
            return [idxs_of_nums_seen[other_num], idx]
        idxs_of_nums_seen[num] = idx


assert two_sum_dict([2, 7, 11, 15], 9) == [0, 1]
assert two_sum_dict([0, 4, 3, 0], 0) == [0, 3]
