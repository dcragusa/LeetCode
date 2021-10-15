"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1. Return the ordering of
courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible
to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1, 0]],  Output: [0, 1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
So the correct course order is [0, 1].

Example 2:
Input: numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],  Output: [0, 2, 1, 3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0, 1, 2, 3]. Another correct ordering is [0, 2, 1, 3].

Example 3:
Input: numCourses = 1, prerequisites = [],  Output: [0]
"""

"""
This is equivalent to finding a topological sort of a directed graph, and in fact the code is almost identical to
problem 207. The only modification is adding the node at the end of the depth-first-search (i.e., a node that has no
prerequisites) to the course order, and working backwards up the depth-first calls. The same mechanism to detect cycles 
in 207 is employed here to return an empty array if no ordering is possible (i.e., if there are cyles in the graph).
"""

from collections import defaultdict


def find_order(numCourses, prerequisites):
    prereq_map = defaultdict(list)
    for course, prereq in prerequisites:
        prereq_map[course].append(prereq)

    course_order = []
    node_colours = [0] * numCourses

    def dfs_visit(node):
        if node_colours[node] == 2:
            return True
        if node_colours[node] == 1:
            return False

        node_colours[node] = 1
        for prereq in prereq_map[node]:
            if not dfs_visit(prereq):
                return False

        node_colours[node] = 2
        course_order.append(node)
        return True

    for course in range(numCourses):
        if not dfs_visit(course):
            return []

    return course_order


assert find_order(2, [[1, 0]]) == [0, 1]
assert find_order(2, [[1, 0], [0, 1]]) == []
assert find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
assert find_order(1, []) == [0]
