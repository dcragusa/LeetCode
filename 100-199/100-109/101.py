"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1, 2, 2, 3, 4, 4, 3]
Output: true

        1
      /   \
    2      2
   / \    / \
  3  4   4   3

Example 2:
Input: root = [1, 2, 2, None, 3, None, 3]
Output: false

    1
   / \
  2   2
   \   \
   3    3
"""

"""
We recursively check whether opposite ends of the tree are equal, going down the tree. 
The logic is very similar to problem 100.
"""

from shared import list_to_tree


def is_symmetric(root):
    def helper(left, right):
        if left is None and right is None:
            return True
        elif left and right:
            return helper(left.left, right.right) and left.val == right.val and helper(left.right, right.left)
        else:
            return False

    return helper(root.left, root.right)


assert is_symmetric(list_to_tree([1, 2, 2, 3, 4, 4, 3])) is True
assert is_symmetric(list_to_tree([1, 2, 2, None, 3, None, 3])) is False
assert is_symmetric(list_to_tree([1, 2, 2, None, 2, None])) is False
assert is_symmetric(list_to_tree([1, 2, 3])) is False
