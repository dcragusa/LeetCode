"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a
distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings
collectively. The geometric information of each building is given in the array buildings where
buildings[i] = [lefti, righti, heighti]:
- lefti is the x coordinate of the left edge of the ith building.
- righti is the x coordinate of the right edge of the ith building.
- heighti is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0. The skyline
should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each
key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which
always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any
ground between the leftmost and rightmost buildings should be part of the skyline's contour.
Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance,
[..., [2 3], [4 5], [7 5], [11 5], [12 7], ...] is not acceptable; the three lines of height 5 should be merged into
one in  the final output as such: [..., [2 3], [4 5], [12 7], ...]

Example 1:
Input: buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
Output: [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]

Example 2:
Input: buildings = [[0, 2, 3], [2, 5, 3]],  Output: [[0, 3], [5, 0]]
"""

"""
For small ranges, we could set up an array of building heights initialised to 0, then simply iterate over the 
buildings segments, updating the max height as appropriate. However, this fails due to space constraints if the input 
range is very large. 
In this case, we can use a heap, which will keep track of the current maximum height for us. Firstly, we obtain a 
sorted list of transition points (either the left or right side of the buildings). We deduplicate using a set. At the 
same time, we build up a dict that maps left transition point to the building. We then iterate across transitions. 
- If any buildings start at the transition point (using the building map we built earlier), we add the negative of the 
height to a heap. We negate the height because we are interested in the maximum height, whereas Python's heap is a 
minimum heap. The heap root will now always be the maximum height building.
- We then pop heap roots that have a right side smaller than the current transition position, as we are past them.
- Finally, we add the transition and height to the results list if the height of the heap root is different from the
previous max height.
"""


# def get_skyline(buildings):
#     rightmost = buildings[-1][1]
#     heights = [0] * (rightmost + 1)
#     for left, right, height in buildings:
#         for i in range(left, right):
#             heights[i] = max(heights[i], height)
#
#     prev = 0
#     results = []
#     for idx, height in enumerate(heights):
#         if height == prev:
#             continue
#         prev = height
#         results.append([idx, height])
#
#     return results


import heapq
from collections import defaultdict


def get_skyline(buildings):
    transitions = set()
    building_map = defaultdict(list)

    for left, right, height in buildings:
        transitions.add(left)
        transitions.add(right)
        building_map[left].append((left, right, height))

    transitions = sorted(list(transitions))
    roof_heap = []
    results = []
    last_height = 0

    for transition in transitions:
        for left, right, height in building_map[transition]:
            heapq.heappush(roof_heap, (-height, right))

        while roof_heap and roof_heap[0][1] <= transition:
            heapq.heappop(roof_heap)

        height = -roof_heap[0][0] if roof_heap else 0
        if height != last_height:
            last_height = height
            results.append([transition, height])

    return results


assert get_skyline([
    [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]
]) == [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
assert get_skyline([[0, 2, 3], [2, 5, 3]]) == [[0, 3], [5, 0]]
assert get_skyline([[0, 2147483647, 2147483647]]) == [[0, 2147483647], [2147483647, 0]]
