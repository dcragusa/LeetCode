"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and
postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9, 3, 15, 20, 7], postorder = [9, 15, 7, 20, 3],  Output: [3, 9, 20, null, null, 15, 7]

     3
   /  \
  9   20
     /  \
   15    7

Example 2:
Input: inorder = [-1], postorder = [-1],  Output: [-1]

Example 3:
Input: inorder = [2, 1, 3], postorder = [2, 3, 1],  Output: [1, 2, 3]

    1
   / \
  2   3
"""

"""
Similar to the logic for 105 (building a tree from preorder and inorder traversal) - but we count back from the end 
of the postorder list (as we know the root will be the last item). We also build the right side before the left.
"""


from shared import TreeNode


def build_tree(inorder, postorder):

    postorder_idx = -1

    def helper(low, high):
        nonlocal postorder_idx
        if low == high:
            return None
        value = postorder[postorder_idx]
        node = TreeNode(value)
        inorder_idx = inorder.index(value, low, high)
        postorder_idx -= 1
        node.right = helper(inorder_idx + 1, high)
        node.left = helper(low, inorder_idx)
        return node

    return helper(0, len(inorder))


tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert build_tree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]) == tree

tree = TreeNode(-1)
assert build_tree([-1], [-1]) == tree

tree = TreeNode(1, TreeNode(2), TreeNode(3))
assert build_tree([2, 1, 3], [2, 3, 1]) == tree
