"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1, 2, 3], q = [1, 2, 3],  Output: true

     1           1
    / \         / \
   2  3   ->   2   3

Example 2:
Input: p = [1, 2], q = [1, None, 2],  Output: false

     1     1
    /       \
   2   ->    2

Example 3:
Input: p = [1, 2, 1], q = [1, 1, 2],  Output: false

     1           1
    / \         / \
   2  1   ->   1   2
"""

"""
We do an inorder traversal of both trees, checking if nodes are equal. There is some special casing for None values.
"""

from shared import list_to_tree


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p and q:
        return is_same_tree(p.left, q.left) and p.val == q.val and is_same_tree(p.right, q.right)
    else:
        return False


assert is_same_tree(list_to_tree([1, 2, 3]), list_to_tree([1, 2, 3])) is True
assert is_same_tree(list_to_tree([1, 2]), list_to_tree([1, None, 2])) is False
assert is_same_tree(list_to_tree([1, 2, 1]), list_to_tree([1, 1, 2])) is False
