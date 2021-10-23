"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4, 2, 7, 1, 3, 6, 9],  Output: [4, 7, 2, 9, 6, 3, 1]

       4             4
      / \           / \
    2    7   ->   7    2
   / \  / \      / \  / \
  1  3 6   9    9  6 3   1

Example 2:
Input: root = [2, 1, 3],  Output: [2, 3, 1]

    2         2
   / \   ->  / \
  1   3     3   1

Example 3:
Input: root = [],  Output: []
"""

"""
Trivial to do recursively: for each node we just swap right and left children.
"""

from shared import list_to_tree


def invert_tree(root):
    if not root:
        return root
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root


assert invert_tree(list_to_tree([4, 2, 7, 1, 3, 6, 9])) == list_to_tree([4, 7, 2, 9, 6, 3, 1])
assert invert_tree(list_to_tree([2, 1, 3])) == list_to_tree([2, 3, 1])
