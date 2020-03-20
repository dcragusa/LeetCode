"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that
a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

"""
First we sort our array and make a dictionary of nums to indices for later O(1) retrieval. Then we iterate across the
array, fixing one number at a time. We can skip a lot of combinations by checking if the target can be reached by any
combination with the current fixed number, or if all the combinations we can form are bigger than the target. When we
fix the final number, we know the exact number we are aiming for. We look that up in our earlier-formed dictionary,
and if the index is larger than the final fixed number, it is a valid combination. We add them as tuples in sets to 
avoid duplicates.
"""


def four_sum(nums, target):
    nums.sort()
    if (len_nums := len(nums)) < 4:
        return []
    max_num = nums[-1]
    nums_to_idx = {j: i for i, j in enumerate(nums)}
    solutions = set()
    for i in range(len_nums-3):
        num_i = nums[i]
        if num_i + 3 * max_num < target:  # cannot reach with current i
            continue
        if num_i * 4 > target:  # passed, no point increasing i
            break
        for j in range(i+1, len_nums-2):
            num_j = nums[j]
            if num_i + num_j + 2 * max_num < target:  # cannot reach with current j
                continue
            if num_i + num_j * 3 > target:  # passed, no point increasing j
                break
            for k in range(j+1, len_nums-1):
                num_k = nums[k]
                difference = target - num_i - num_j - num_k
                if difference < num_k:  # passed, no point increasing k
                    break
                if difference in nums_to_idx and nums_to_idx[difference] > k:  # the difference exists and is after k
                    solutions.add((num_i, num_j, num_k, difference))
    return solutions


assert four_sum([-3, -2, -1, 0, 0, 1, 2, 3], 0) == {
    (-3, -2, 2, 3), (-2, -1, 0, 3), (-2, 0, 0, 2), (-2, -1, 1, 2),
    (-3, -1, 1, 3), (-3, 0, 1, 2), (-1, 0, 0, 1), (-3, 0, 0, 3)
}
assert four_sum([5, 5, 3, 5, 1, -5, 1, -2], 0) == {(-5, 1, 1, 3)}
assert four_sum([-5, -4, -2, -2, -2, -1, 0, 0, 1], -9) == {
    (-4, -2, -2, -1), (-5, -4, 0, 0), (-5, -4, -1, 1), (-5, -2, -2, 0)
}
