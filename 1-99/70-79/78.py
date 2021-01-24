"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3],  Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
"""

"""
We take advantage of itertools.combinations that does this for us, with all combination lengths from 0 to len(nums).
"""


from itertools import combinations


def subsets(nums):
    results = []
    for i in range(len(nums)+1):
        for combination in combinations(nums, i):
            results.append(list(combination))
    return results


assert subsets([1, 2, 3]) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
