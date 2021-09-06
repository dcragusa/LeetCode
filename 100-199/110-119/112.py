"""
Given the root of a binary tree and an integer `target_sum`, return `True` if the tree has a root-to-leaf path
such that adding up all the values along the path equals `target_sum`. A leaf is a node with no children.

Example 1:
Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], target_sum = 22,  Output: true (5 + 4 + 11 + 2)

         5
       /  \
      4    8
     /    / \
    11   13  4
   / \        \
  7   2        1

Example 2:
Input: root = [1, 2, 3], target_sum = 5,  Output: false

    1
   / \
  2   3

Example 3:
Input: root = [1, 2], target_sum = 0,  Output: false

    1
   /
  2
"""

"""
We decrement target_sum as we recur down the list. If we find a leaf node equal to target_sum, then there is a path.
"""

from shared import TreeNode


def has_path_sum(root, target_sum):
    if root is None:
        return False
    if root.left is None and root.right is None and root.val == target_sum:
        return True
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(root.right, target_sum - root.val)


root = TreeNode(
    5,
    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
    TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
)
assert has_path_sum(root, 22) is True

root = TreeNode(1, TreeNode(2), TreeNode(3))
assert has_path_sum(root, 5) is False

root = TreeNode(1, TreeNode(2))
assert has_path_sum(root, 0) is False

root = TreeNode(-2, None, TreeNode(-3))
assert has_path_sum(root, -5) is True

root = TreeNode(8, TreeNode(9), TreeNode(-6, TreeNode(5), TreeNode(9)))
assert has_path_sum(root, 7) is True
