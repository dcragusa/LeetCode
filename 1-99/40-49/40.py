"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8,
A solution set is: [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]

Example 2:
Input: candidates = [2, 5, 2, 1, 2], target = 5,
A solution set is: [[1, 2, 2], [5]]
"""

"""
Similar to problem 39, we go through the set of candidates one at a time, subtracting the number from the target.
If there is no remainder, that is a combination. We then recur with all higher candidates. This ensures we check 
every possible combination. We can skip duplicate numbers, as we have already checked all combinations with those 
on previous iterations.
"""


def combination_sum2(candidates, target):
    combinations = []
    candidates.sort()
    for idx_num, num in enumerate(candidates):
        if num > target:
            continue
        if idx_num and num == candidates[idx_num-1]:
            continue
        remainder = target - num
        if not remainder:
            combinations.append([num])
        else:
            for combination in combination_sum2(candidates[idx_num+1:], remainder):
                combinations.append([num] + combination)
    return combinations


assert combination_sum2([10, 1, 2, 7, 6, 1, 5], 8) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
assert combination_sum2([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]
