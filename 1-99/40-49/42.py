"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

Example:
Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],  Output: 6

3               |
2       | w w w | | w |
1 - | w | | w | | | | | |
"""

"""
First we find the index of the maximum of the array (it doesn't matter if there is more than one). Then we divide the
array in two halves split on the index, counting forward and backward with a local maximum. If the wall is lower than
the local maximum, we add (local max - wall height) to a counter, and if the wall is equal or higher to the local
maximum, we add the counter to the total water count and reset the counter to 0.
"""


def trap(heights):
    if not heights:
        return 0
    max_wall_idx = heights.index(max(heights))
    total_water = water = 0
    for bisected in [heights[:max_wall_idx+1], reversed(heights[max_wall_idx:])]:
        current_max = 0
        for wall in bisected:
            if wall >= current_max:
                current_max = wall
                total_water += water
                water = 0
            else:
                water += current_max - wall
    return total_water


assert trap([]) == 0
assert trap([1]) == 0
assert trap([12]) == 0
assert trap([121]) == 0
assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
