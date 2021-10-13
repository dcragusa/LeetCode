"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1, 0]],  Output: True
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]],  Output: False
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.
"""

"""
This is equivalent to finding a cycle in a directed graph, where the nodes are courses and prerequisites are edges.
We implement the graph-colouring algorithm from CLRS: we first process the prerequisites into a dict of node: prereqs.
Then we set up a list containing the colours for each node (for simplicity, white, grey, and black are 0, 1, 2 here).
Finally, for each white node, the colour is set to grey, a depth-first-search for all neighbours is performed, and 
finally the colour is set to black before moving on. Detecting cycles can be done if we find a grey node during the 
DFS - if such a node is detected, we return early as the scheduling is impossible.
"""

from collections import defaultdict


def can_finish(numCourses, prerequisites):
    prereq_map = defaultdict(list)
    for course, prereq in prerequisites:
        if course == prereq:
            return False
        prereq_map[course].append(prereq)

    node_colours = [0] * numCourses

    def dfs_visit(node):
        node_colours[node] = 1
        for prereq in prereq_map[node]:
            if node_colours[prereq] == 1:
                return False
            elif node_colours[prereq] == 0 and not dfs_visit(prereq):
                return False
        node_colours[node] = 2
        return True

    for course in range(numCourses):
        if node_colours[course] == 0:
            if not dfs_visit(course):
                return False

    return True


assert can_finish(2, [[1, 0]]) is True
assert can_finish(2, [[1, 0], [0, 1]]) is False
assert can_finish(10, [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9]]) is True
assert can_finish(11, [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9], [8, 10]]) is True
assert can_finish(11, [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9], [8, 10], [3, 10]]) is True
assert can_finish(3, [[0, 1], [0, 2], [1, 2]]) is True
