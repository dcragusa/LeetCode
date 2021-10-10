"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer
array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight
without alerting the police.

Example 1:
Input: nums = [1, 2, 3, 1],  Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2, 7, 9, 3, 1],  Output: 12
Explanation: Rob house 1 (money = 2),  rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

"""
We use DP to solve this problem - we can re-use the same input array to save space. We first special-case the first two
items of the array, then iterate across the array. At each step we set the maximum of the item two spots ago plus the 
current item (leaving a gap), or the item one spot ago. This ensures that we never pick from houses next to each other.
When we have finished iterating, the maximum profit will be at the end of the array.
"""


def rob(nums):

    if (len_nums := len(nums)) < 3:
        return max(nums)

    nums[1] = max(nums[:2])
    for i in range(2, len_nums):
        nums[i] = max(nums[i-2] + nums[i], nums[i-1])
    return nums[-1]


assert rob([1, 2, 3, 1]) == 4
assert rob([2, 7, 9, 3, 1]) == 12
