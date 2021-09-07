"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
Input:
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7],  Output: 49
Explanation:
h[1] = 8, h[8] = 7, area is min(8, 7) * (8-1) = 7*7 = 49
"""

"""
We start with taking each end of the list, for the widest possible bucket. We move inwards, moving the smaller end
each time (if we move the larger end, we are guaranteed a smaller bucket). 
"""


def find_max_area(heights):
    start_idx, end_idx = 0, len(heights) - 1
    max_area = min(heights[0], heights[end_idx]) * end_idx
    while start_idx < end_idx:
        if heights[start_idx] < heights[end_idx]:
            start_idx += 1
        else:
            end_idx -= 1
        max_area = max(max_area, min(heights[start_idx], heights[end_idx]) * (end_idx - start_idx))
    return max_area


assert find_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert find_max_area([2, 3, 4, 5, 18, 17, 6]) == 17
