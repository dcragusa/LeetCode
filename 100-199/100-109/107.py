"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
(i.e., from left to right, level by level from leaf to root).

Example 1:
Input: root = [3, 9, 20, None, None, 15, 7],  Output: [[15, 7], [9, 20], [3]]

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
Identical to 102, except we reverse the by-level list when reading off at the end.
"""

from collections import defaultdict
from shared import list_to_tree


def level_order_bottom(root):
    levels = defaultdict(list)

    def helper(node, position):
        if node is None:
            return
        levels[position].append(node.val)
        helper(node.left, position + 1)
        helper(node.right, position + 1)

    helper(root, 1)
    return list(levels.values())[::-1]


assert level_order_bottom(list_to_tree([3, 9, 20, None, None, 15, 7])) == [[15, 7], [9, 20], [3]]
assert level_order_bottom(list_to_tree([1])) == [[1]]
assert level_order_bottom(list_to_tree([])) == []
