"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output: [[2], [1], [1,2,2], [2,2], [1,2], []]
"""

"""
Similarly to problem 78, we take advantage of itertools.combinations that does this for us, with all combination 
lengths from 0 to len(nums). However this time we sort the array to exclude repeated results and check if we have
previously obtained that combination by using a set.
"""

from itertools import combinations


def subsets(nums):
    results = []
    seen = set()
    for i in range(len(nums) + 1):
        for combination in combinations(sorted(nums), i):
            if combination not in seen:
                seen.add(combination)
                results.append(list(combination))
    return results


assert subsets([1, 2, 2]) == [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
assert subsets([4, 4, 4, 1, 4]) == [
    [], [1], [4], [1, 4], [4, 4], [1, 4, 4], [4, 4, 4], [1, 4, 4, 4], [4, 4, 4, 4], [1, 4, 4, 4, 4]
]
