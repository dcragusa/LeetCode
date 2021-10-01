"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number
of points that lie on the same straight line.

Example 1:
Input: points = [[1, 1], [2, 2], [3, 3]],  Output: 3

Example 2:
Input: points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],  Output: 4
"""

"""
To solve this we have to remember the line equations: y = mx + c and m = (y2-y1)/(x2-x1). We can then define each line
uniquely by its gradient m and intercept c. To get c we can rearrange the gradient equation to get c = y1 + m(x1).
Having established this, we go through the list of points and compare each to the points after it in the list to
compare all combinations of two points. For each pair, we obtain the gradient and intercept (for simplicity, when the
line is vertical, the intercept is returned as the x-axis intercept instead of the usual y-axis intercept). This is
saved in a dict. The first time it is found, 2 is added (due to the 2 points), and subsequently as new points are 
found, 1 is added. We also add points found to a set corresponding to each equation: if both points are in that set,
we have examined each of them in relation to some other point, so we do not add anything to the equations dict.
Once we have been through the entire list, we merely return the largest number in the equations dict.
"""

from collections import defaultdict


def max_points(points):

    def get_equation(p1, p2):
        if (diff_x := p2[0] - p1[0]) == 0:
            return None, p1[0]
        gradient = (p2[1] - p1[1]) / diff_x
        return gradient, p1[1] - (gradient * p1[0])

    if len(points) == 1:
        return 1

    points = [tuple(point) for point in points]
    equations = defaultdict(int)
    seen_lines = defaultdict(set)

    for idx, p1 in enumerate(points):
        for p2 in points[idx+1:]:
            equation = get_equation(p1, p2)
            if p1 in seen_lines[equation] and p2 in seen_lines[equation]:
                continue
            points_to_add = 2 if equation not in equations else 1
            equations[equation] += points_to_add
            seen_lines[equation].add(p1)
            seen_lines[equation].add(p2)

    return max(equations.values())


assert max_points([[1, 1], [2, 2], [3, 3]]) == 3
assert max_points([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
assert max_points([[2, 3], [3, 3], [-5, 3]]) == 3
assert max_points([[0, 0], [4, 5], [7, 8], [8, 9], [5, 6], [3, 4], [1, 1]]) == 5



