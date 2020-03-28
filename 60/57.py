"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5],  Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8],  Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

"""
If there are no current intervals, or the new upper is smaller than the smallest existing lower, we return the new 
interval + any existing intervals. We then proceed to find where the new interval should slot in by iterating across 
the intervals. If the new lower is higher than the current upper, it must slot into a later interval. Once found, 
we find where the new upper should merge into. We do this by iterating across the remaining intervals, and finding 
the first lower which is higher than the new upper - this means the new upper should slot into the previous interval.
We add a guard of infinite value to make sure the check succeeds even if the upper should have to merge into the last 
interval. Once we have found the lower and upper insertion points, we simply reconstruct the list to return.
"""


def insert(intervals, new_interval):
    if not intervals or new_interval[1] < intervals[0][0]:
        return [new_interval] + intervals
    intervals.append([float('inf'), float('inf')])
    for idx, interval in enumerate(intervals[:-1]):
        if new_interval[0] > interval[1]:
            continue
        for other_idx, other_interval in enumerate(intervals[idx:], start=idx):
            if new_interval[1] >= other_interval[0]:
                continue
            start = intervals[:idx]
            middle = [[min(new_interval[0], interval[0]), max(new_interval[1], intervals[other_idx-1][1])]]
            end = intervals[other_idx:-1]
            return start + middle + end
    return intervals[:-1] + [new_interval]


assert insert([], [5, 7]) == [[5, 7]]
assert insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]]
assert insert([[1, 5]], [0, 3]) == [[0, 5]]
assert insert([[1, 5]], [5, 7]) == [[1, 7]]
assert insert([[1, 5]], [6, 7]) == [[1, 5], [6, 7]]
assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
assert insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
