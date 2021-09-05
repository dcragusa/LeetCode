"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3],  Output: true

     1           1
    / \         / \
   2  3   ->   2   3

Example 2:
Input: p = [1,2], q = [1,null,2],  Output: false

     1     1
    /       \
   2   ->    2

Example 3:
Input: p = [1,2,1], q = [1,1,2],  Output: false

     1           1
    / \         / \
   2  1   ->   1   2
"""

"""
We do an inorder traversal of both trees, checking if nodes are equal. There is some special casing for None values.
"""

from shared import TreeNode


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p and q:
        return is_same_tree(p.left, q.left) and p.val == q.val and is_same_tree(p.right, q.right)
    else:
        return False


p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
assert is_same_tree(p, q) is True

p = TreeNode(1, TreeNode(2), None)
q = TreeNode(1, None, TreeNode(2))
assert is_same_tree(p, q) is False

p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))
assert is_same_tree(p, q) is False
