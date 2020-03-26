"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]], Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]], Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

"""
We first sort the list of intervals so they are in ascending order. Sorting the list first means we never have to 
check the lower part of the last result, as we are guaranteed the subsequent lowers will be either within the last 
result - in which case we check the upper to see if the last result can be extended or the current interval skipped - 
or higher than it - in which case it is a new interval and we add it to the results.
"""


def merge_intervals(intervals):
    results = []
    if not intervals:
        return results
    intervals.sort()
    for interval in intervals:
        if not results or interval[0] > results[-1][1]:
            results.append(interval)
        elif interval[1] > results[-1][1]:
            results[-1][1] = interval[1]
    return results


assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
assert merge_intervals([[1, 4], [0, 5]]) == [[0, 5]]
assert merge_intervals([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
assert merge_intervals([[2, 3], [4, 6], [5, 7], [3, 4]]) == [[2, 7]]
assert merge_intervals(
    [[2, 3], [5, 7], [0, 1], [4, 6], [5, 5], [4, 6], [5, 6], [1, 3], [4, 4], [0, 0], [3, 5], [2, 2]]) == [[0, 7]]
assert merge_intervals(
    [[3, 5], [0, 0], [4, 4], [0, 2], [5, 6], [4, 5], [3, 5], [1, 3], [4, 6], [4, 6], [3, 4]]) == [[0, 6]]
