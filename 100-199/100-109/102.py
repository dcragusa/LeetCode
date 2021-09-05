"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
Input: root = [3, 9, 20, null, null, 15, 7],  Output: [[3], [9, 20], [15, 7]]

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

from shared import TreeNode
from collections import defaultdict


def level_order(root):

    levels = defaultdict(list)

    def helper(node, position):
        if node is None:
            return
        levels[position].append(node.val)
        helper(node.left, position+1)
        helper(node.right, position+1)

    helper(root, 1)
    return list(levels.values())


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert level_order(root) == [[3], [9, 20], [15, 7]]

root = TreeNode(1)
assert level_order(root) == [[1]]

root = None
assert level_order(root) == []
