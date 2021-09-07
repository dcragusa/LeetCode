"""
Given the root of a binary tree and an integer `target_sum`, return `True` if the tree has a root-to-leaf path
such that adding up all the values along the path equals `target_sum`. A leaf is a node with no children.

Example 1:
Input: root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], target_sum = 22,  Output: true (5 + 4 + 11 + 2)

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

from shared import list_to_tree


def has_path_sum(root, target_sum):
    if root is None:
        return False
    if root.left is None and root.right is None and root.val == target_sum:
        return True
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(root.right, target_sum - root.val)


assert has_path_sum(list_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22) is True
assert has_path_sum(list_to_tree([1, 2, 3]), 5) is False
assert has_path_sum(list_to_tree([1, 2]), 0) is False
assert has_path_sum(list_to_tree([-2, None, -3]), -5) is True
assert has_path_sum(list_to_tree([8, 9, -6, None, None, 5, 9]), 7) is True
