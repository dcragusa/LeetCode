"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Input: [2, 1, 3],  Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5, 1, 4, None, None, 3, 6],  Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

"""
For each node, we obtain the min and max of the left and right side values respectively. If the left max is larger or
the right min is smaller than the node, the tree is invalid. We then propagate the min and max of the node val and the
previously obtained min/maxes upwards. We take when returning the result that a tuple evaluates to True.
"""

from shared import list_to_tree


def is_valid_bst(root):
    if root is None or root.val is None:
        return True

    def recur(node):
        vals = [node.val]
        if node.left:
            recur_left = recur(node.left)
            if not recur_left or recur_left[1] >= node.val:
                return False
            vals.extend(recur_left)
        if node.right:
            recur_right = recur(node.right)
            if not recur_right or recur_right[0] <= node.val:
                return False
            vals.extend(recur_right)
        return min(vals), max(vals)

    return bool(recur(root))


assert is_valid_bst(None) is True
assert is_valid_bst(list_to_tree([None])) is True
assert is_valid_bst(list_to_tree([2, 1, 3])) is True
assert is_valid_bst(list_to_tree([5, 1, 4, None, None, 3, 6])) is False

#    10
#   /  \
#  5   15
#     /  \
#    6   20
assert is_valid_bst(list_to_tree([10, 5, 15, None, None, 6, 20])) is False
