"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:
Input: n = 4, k = 2,  Output: [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]
"""

"""
Batteries included with itertools.combinations. An alternative implementation is provided.
"""

from itertools import combinations


def combine_batteries_included(n, k):
    return [list(combination) for combination in combinations(range(1, n+1), k)]


def combine(n, k):
    result = []
    pool, indices = list(range(1, n+1)), list(range(k))
    result.append([pool[i] for i in indices])
    while True:
        for i in reversed(range(k)):
            if indices[i] != i + n - k:
                break
        else:
            return result
        indices[i] += 1
        for j in range(i+1, k):
            indices[j] = indices[j-1] + 1
        result.append([pool[i] for i in indices])


assert combine_batteries_included(4, 2) == combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
