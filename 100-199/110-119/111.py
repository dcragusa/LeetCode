"""
Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node. Note: A leaf is a node with no children.

Example 1:
Input: root = [3, 9, 20, None, None, 15, 7],  Output: 2

    3
   / \
  9  20
    /  \
   15   7

Example 2:
Input: root = [1, 2, 2, 3, 3, None, None, 4, 4],  Output: 2

        1
       / \
      2   2
     / \
    3   3
   / \
  4   4

Example 3:
Input: root = [1, 2, None, 3, None, 4, None, 5],  Output: 5

          1
         /
        2
       /
      3
     /
    4
   /
  5
"""

"""
Since we are trying to find the minimum depth, a breadth-first search is more appropriate here. This is implemented
by a deque (for fast pops on the left end). As soon as we find a leaf node (both children are None), return the depth.
"""

from collections import deque
from shared import list_to_tree


def min_depth(root):
    if root is None:
        return 0

    queue = deque([(root, 1)])
    while queue:
        node, level = queue.popleft()
        if not node.left and not node.right:
            return level
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))


assert min_depth(list_to_tree([3, 9, 20, None, None, 15, 7])) == 2
assert min_depth(list_to_tree([1, 2, 2, 3, 3, None, None, 4, 4])) == 2
assert min_depth(list_to_tree([1, 2, None, 3, None, 4, None, 5])) == 5
assert min_depth(list_to_tree([])) == 0
