"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3, 9, 20, null, null, 15, 7],  Output: 3

     3
   /  \
  9   20
     /  \
   15    7


Example 2:
Input: root = [1,null,2],  Output: 2

  1
   \
    2

Example 3:
Input: root = [],  Output: 0

Example 4:
Input: root = [0],  Output: 1
"""

"""
Recur down the tree, saving the maximum depth as we go. Once finished, return max depth.
"""

from shared import TreeNode


def find_max_depth(root):

    max_depth = 0

    def helper(node, depth):
        nonlocal max_depth
        if node is None:
            return
        helper(node.left, depth+1)
        max_depth = max(max_depth, depth)
        helper(node.right, depth+1)

    helper(root, 1)
    return max_depth


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert find_max_depth(root) == 3

root = TreeNode(1, None, TreeNode(2))
assert find_max_depth(root) == 2

root = None
assert find_max_depth(root) == 0

root = TreeNode(1)
assert find_max_depth(root) == 1
