"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area
of the largest rectangle in the histogram.

      #
    # #
    # #
    # #   -
-   # # - -
- - # # - -

Example (as above):
Input: [2,1,5,6,2,3],  Output: 10
"""

"""
We iterate through the bars, keeping a stack of increasing height indices. If the next bar is the same height or 
taller, the maximum area is guaranteed to increase so we do not need to calculate it yet. If the next bar is shorter, 
we must update the max area. To calculate the max area, we pop off the top value from the stack. This is the max 
height of the rectangle. The left boundary of the rectangle is the current top value of the stack, and the right edge 
is i-1. We then update the max_area according to height * (right - left). We repeat this procedure until the stack no 
longer has heights taller than the current one.
"""


def largest_rectangle_area(heights):
    max_area = 0
    heights.append(0)
    stack = [-1]
    for idx, val in enumerate(heights):
        while heights[idx] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = idx - 1 - stack[-1]
            max_area = max(max_area, height*width)
        stack.append(idx)
    return max_area


assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
assert largest_rectangle_area(list(range(20000))) == 100000000
