"""
Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is defined as a binary tree
in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [3, 9, 20, null, null, 15, 7],  Output: true

    3
   / \
  9  20
    /  \
   15   7

Example 2:
Input: root = [1, 2, 2, 3, 3, null, null, 4, 4],  Output: false

        1
       / \
      2   2
     / \
    3   3
   / \
  4   4

Example 3:
Input: root = [],  Output: true
"""

"""
We recurse down the tree, passing up the maximum depth of the nodes. We check if the left and right subtrees
differ by more than one at each step, passing any failures upwards.
"""

from shared import TreeNode


def is_balanced(root):

    def helper(node):
        if node is None:
            return True, 0
        left, right = helper(node.left), helper(node.right)
        if left[0] and right[0]:
            return abs(left[1] - right[1]) <= 1, max(left[1], right[1]) + 1
        else:
            return False, -1

    return helper(root)[0]


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert is_balanced(root) is True

root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
assert is_balanced(root) is False

root = None
assert is_balanced(root) is True
