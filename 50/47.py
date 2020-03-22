"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2], Output: [[1,1,2], [1,2,1], [2,1,1]]
"""

"""
We use the same principle from problem 46, skipping any numbers we have already fixed. This eliminates any duplicates.
"""


def unique_permutations(nums):
    if len(nums) <= 1:
        return [nums]
    else:
        combinations = []
        nums_seen = set()
        for idx, num in enumerate(nums):
            if num in nums_seen:
                continue
            partial_list = nums[:idx] + nums[idx+1:]
            combinations.extend([[num] + combination for combination in unique_permutations(partial_list)])
            nums_seen.add(num)
        return combinations


assert unique_permutations([]) == [[]]
assert unique_permutations([1]) == [[1]]
assert unique_permutations([1, 1]) == [[1, 1]]
assert unique_permutations([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
