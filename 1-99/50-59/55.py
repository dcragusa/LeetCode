"""
You are given an array of non-negative integers, and are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length from that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2, 3, 1, 1, 4],  Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3, 2, 1, 0, 4],  Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

"""
We iterate through the list and keep a running track of the maximum index we can reach from that position (current 
index + current value). If at some point we reach an index higher than the maximum, the last index is not reachable.
We can terminate the iteration early if we observe the max index reaching the last index.
"""


def can_jump(nums):
    if len(nums) <= 1:
        return True
    max_idx = 0
    for idx, val in enumerate(nums):
        if idx > max_idx:
            return False
        max_idx = max(max_idx, idx+val)
        if max_idx >= len(nums) - 1:
            return True


assert can_jump([2, 0, 0]) is True
assert can_jump([2, 1, 2, 0, 4]) is True
assert can_jump([2, 3, 1, 1, 4]) is True
assert can_jump([3, 2, 1, 0, 4]) is False
