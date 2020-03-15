"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to
target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

"""
First we sort the array, then we fix one number and examine the rest of the array from opposite ends, going inwards.
If the difference of the total is less than the current difference, we update the difference. Finally, we return the
target minus the difference, which is the closest we can get. We can skip some iterations if we have already fixed a 
number (as we have already checked all possible combinations from the previous run).
"""


def three_sum_closest(nums, target):
    nums.sort()
    closest_diff = float('inf')
    for fixed_idx, fixed_num in enumerate(nums[:-2]):
        if fixed_idx >= 1 and fixed_num == nums[fixed_idx-1]:
            # we have already checked this fixed number, so we can skip
            continue
        low_idx, high_idx = fixed_idx+1, len(nums)-1
        while low_idx < high_idx:
            difference = target - (this_sum := (nums[low_idx] + nums[high_idx] + fixed_num))
            if not difference:
                return this_sum
            if difference > 0:
                low_idx += 1
            else:
                high_idx -= 1
            if abs(difference) < abs(closest_diff):
                closest_diff = difference
    return target - closest_diff


assert three_sum_closest([1, 2, 3], 3) == 6
assert three_sum_closest([-1, 2, 1, -4], 1) == 2
assert three_sum_closest([1, 1, 1, 0], -100) == 2
assert three_sum_closest([0, 2, 1, -3], 1) == 0
assert three_sum_closest([1, 2, 4, 8, 16, 32, 64, 128], 82) == 82

