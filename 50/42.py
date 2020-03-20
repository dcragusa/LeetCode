"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1], Output: 6

3               |
2       | w w w | | w |
1 - | w | | w | | | | | |
"""


def trap(heights):
    if not heights:
        return 0
    max_wall_idx = heights.index(max(heights))
    total_water = water = 0
    for bisected in [range(max_wall_idx), range(-1, -(len(heights)-max_wall_idx+1), -1)]:
        current_max = 0
        for idx in bisected:
            if (wall := heights[idx]) >= current_max:
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
