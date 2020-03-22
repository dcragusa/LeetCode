"""
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3], Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
"""

"""
Batteries included with itertools.permutations. An alternate implementation is provided, 
which recursively fixes one number at a time and deals with the rest of the list.
"""


def permutations(nums):
    if len(nums) <= 1:
        return [nums]
    elif len(nums) == 2:
        return [nums, [nums[1], nums[0]]]
    else:
        combinations = []
        for idx, num in enumerate(nums):
            combinations.extend([[num] + combination for combination in permutations(nums[:idx] + nums[idx+1:])])
        return combinations


assert permutations([]) == [[]]
assert permutations([1]) == [[1]]
assert permutations([1, 2]) == [[1, 2], [2, 1]]
assert permutations([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
