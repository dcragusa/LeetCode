"""
You are given an array of non-negative integers, and are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length from that position.
Return the fewest number of jumps to reach the last index. You can assume that you can always reach the last index.

Example:
Input: [2,3,1,1,4], Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
             Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

"""
Because we can choose any number of steps at each index, all we have to do is ensure that at each step we pick the jump
that gives us the greatest range (being the current jump + the max of the next jump at that index).
"""


def find_fewest_jumps(nums):
    if len(nums) <= 1:
        return 0
    jumps, idx = 0, 0
    while True:
        if idx + nums[idx] >= len(nums) - 1:
            return jumps + 1
        reach, temp_idx = 0, idx
        for step, next_step in enumerate(nums[idx+1:idx+1+nums[idx]], start=1):
            if (step_reach := step + next_step) > reach:
                reach = step_reach
                temp_idx = idx + step
        idx = temp_idx
        jumps += 1


assert find_fewest_jumps([1]) == 0
assert find_fewest_jumps([1, 1]) == 1
assert find_fewest_jumps([2, 1]) == 1
assert find_fewest_jumps([2, 1, 1]) == 1
assert find_fewest_jumps([1, 2, 3]) == 2
assert find_fewest_jumps([1, 1, 1, 1]) == 3
assert find_fewest_jumps([2, 3, 1, 1, 4]) == 2
assert find_fewest_jumps([2, 3, 0, 1, 4]) == 2
assert find_fewest_jumps([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]) == 3
assert find_fewest_jumps([5, 6, 5, 3, 9, 8, 3, 1, 2, 8, 2, 4, 8, 3, 9, 1, 0, 9, 4, 6, 5, 9, 8, 7, 4, 2, 1, 0, 2]) == 5
