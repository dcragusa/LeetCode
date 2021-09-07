"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2, 3, 6, 7], target = 7,
A solution set is: [[7], [2, 2, 3]]

Example 2:
Input: candidates = [2, 3, 5], target = 8,
A solution set is: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
"""

"""
We go through the set of candidates one at a time, dividing the target by the number. If there is no remainder, 
that is a combination. We then decrease the target by one multiple of the number each time, and recur with all higher
candidates. This ensures we check every possible combination.
"""


def combination_sum(candidates, target):
    combinations = []
    for idx_num, num in enumerate(candidates):
        if num > target:
            continue
        quotient, remainder = divmod(target, num)
        if not remainder:
            combinations.append([num]*quotient)
        for quot_multiple in range(1, quotient+1):
            for combination in combination_sum(candidates[idx_num+1:], target-(quot_multiple*num)):
                combinations.append([num]*quot_multiple + combination)
    return combinations


assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
assert combination_sum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
