"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of
each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2], Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1], Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3], Output: 3
"""

"""
We can re-use our solution for problem 198. We simply have to do it twice - one pass considering the second house
onwards, and another pass from the first house but with the last house set to 0 value. We then take the maximum of
these two passes.
"""


def rob_single(nums):

    if (len_nums := len(nums)) < 3:
        return max(nums)

    dp = [0] * len_nums
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len_nums):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    return dp[-1]


def rob(nums):

    if len(nums) < 3:
        return max(nums)

    second = rob_single(nums[1:])
    nums[-1] = 0
    first = rob_single(nums)
    return max(first, second)


assert rob([2, 3, 2]) == 3
assert rob([1, 2, 3, 1]) == 4
assert rob([1, 2, 3]) == 3
