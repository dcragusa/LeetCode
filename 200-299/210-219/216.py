"""
Find all valid combinations of k numbers that sum up to n such that only numbers 1 through 9 are used, and each number
is used at most once. Return a list of all possible valid combinations. The list must not contain the same combination
twice, and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7,  Output: [[1, 2, 4]]
Explanation:
1 + 2 + 4 = 7

Example 2:
Input: k = 3, n = 9,  Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9

Example 3:
Input: k = 4, n = 1,  Output: []
Using 4 different numbers the smallest sum we can get is 1+2+3+4 = 10 so there is no valid combination.

Example 4:
Input: k = 3,  n = 2,  Output: []

Example 5:
Input: k = 9, n = 45,  Output: [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
"""

"""
Trivial with itertools.combinations - we generate all possible combinations of k then filter for sums equal to n.
Otherwise, we implement a DFS where we fix one number at a time and try to reach an updated target, keeping track of
previously selected numbers to avoid double-counting. When we are at the last level, we append to the list of results
if the target is a valid number.
"""

# from itertools import combinations
#
#
# def combination_sum_3(k, n):
#     all_combinations = list(combinations(range(1, 10), k))
#     return [list(combo) for combo in all_combinations if sum(combo) == n]


def combination_sum_3(k, n):

    results = []

    def helper(level, target, combination):
        nonlocal results
        lowest = combination[-1] + 1 if combination else level
        if level == k:
            if lowest <= target <= 9 and target not in combination:
                results.append(combination + [target])
            return
        for i in range(lowest, 10):
            if i < target and i not in combination:
                helper(level+1, target-i, combination + [i])

    helper(1, n, [])
    return results


assert combination_sum_3(1, 8) == [[8]]
assert combination_sum_3(2, 5) == [[1, 4], [2, 3]]
assert combination_sum_3(3, 7) == [[1, 2, 4]]
assert combination_sum_3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
assert combination_sum_3(4, 1) == []
assert combination_sum_3(3, 2) == []
assert combination_sum_3(9, 45) == [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
