"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3, 9, 20, None, None, 15, 7],  Output: [[3], [20, 9], [15, 7]]

     3
   /  \
  9   20
     /  \
   15    7

Example 2:
Input: root = [1],  Output: [[1]]

Example 3:
Input: root = [],  Output: []
"""

"""
Basically identical to 102 except we read reversed position lists when necessary.
"""

from collections import defaultdict
from shared import list_to_tree


def level_order(root):
    levels = defaultdict(list)

    def helper(node, position):
        if node is None:
            return
        levels[position].append(node.val)
        helper(node.left, position + 1)
        helper(node.right, position + 1)

    helper(root, 1)
    return [vals[::(-1 if idx % 2 else 1)] for idx, vals in enumerate(levels.values())]


assert level_order(list_to_tree([3, 9, 20, None, None, 15, 7])) == [[3], [20, 9], [15, 7]]
assert level_order(list_to_tree([1])) == [[1]]
assert level_order(list_to_tree([])) == []
