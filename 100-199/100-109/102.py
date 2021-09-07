"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
Input: root = [3, 9, 20, None, None, 15, 7],  Output: [[3], [9, 20], [15, 7]]

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
We do an in-order traversal of the tree, saving the level as we go. Then we merely read off the levels at the end.
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
    return list(levels.values())


assert level_order(list_to_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
assert level_order(list_to_tree([1])) == [[1]]
assert level_order(list_to_tree([])) == []
