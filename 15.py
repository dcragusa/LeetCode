"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4], the solution set is: [[-1, 0, 1], [-1, -1, 2]]
"""

"""
First we create a Counter, then sort a list we get from the keys to the counter (this eliminates any doubles). 
We then iterate across the list. If the number has a double, the solution is easy to obtain. If the number has no 
doubles, we take advantage of a variation of two_sum (from problem 1). We can narrow the search space using bisect to 
[current number ... -2*current number]. This is because, as there cannot be a lower number than num due to the array 
being sorted, the maximum number in order to be able to form a triplet is -2*num. We only have to do this bisection
for negative numbers (as for obvious reasons, we need a negative number to make a triplet unless we have 3 zeros).
"""

import bisect
from collections import Counter


def two_sum(nums, target):
    nums_seen = set()
    for num in nums:
        if (other_num := target - num) in nums_seen:
            yield sorted([-target, num, other_num])
        nums_seen.add(num)


def three_sum(nums):
    counts = Counter(nums)
    nums = sorted(counts)
    solutions = []
    for i, num in enumerate(nums):
        if counts[num] >= 2:
            if num == 0:
                if counts[0] >= 3:
                    solutions.append([num] * 3)
            elif -2 * num in nums:
                solutions.append([num, num, -2 * num])
        if num < 0:
            right = bisect.bisect_left(nums, -num * 2)
            solutions.extend(two_sum(nums[i + 1:right], -num))
    return solutions


assert three_sum([0, 0, 0, 0, 0]) == [[0, 0, 0]]
assert three_sum([1, 2, -2, -1]) == []
assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert three_sum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]
