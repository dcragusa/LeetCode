"""
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
The rectangles are defined by bottom-left corners (ax1, ay1), (bx1, by1) and top-right corners (ax2, ay2), (bx2, by2).

Example 1:
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2,  Output: 45

Example 2:
Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2,  Output: 16
"""

"""
We return the sum of the areas of the rectangles minus any intersection area. We see if there is any intersection by
taking the maximum left value and minimum right value (and same for top and bottom). If the maximum left is smaller
than the minimum right and same for top and bottom, there is an intersection so we calculate this area and subtract it.
"""


def compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):

    max_left, min_right = max(ax1, bx1), min(ax2, bx2)
    min_top, max_bottom = min(ay2, by2), max(ay1, by1)

    area_1 = (ax2 - ax1) * (ay2 - ay1)
    area_2 = (bx2 - bx1) * (by2 - by1)

    intersection = 0
    if (max_left < min_right) and (max_bottom < min_top):
        intersection = (min_right - max_left) * (min_top - max_bottom)

    return area_1 + area_2 - intersection


assert compute_area(-3, 0, 3, 4, 0, -1, 9, 2) == 45
assert compute_area(-2, -2, 2, 2, -2, -2, 2, 2) == 16
