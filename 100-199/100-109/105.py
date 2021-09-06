"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7],  Output: [3, 9, 20, null, null, 15, 7]

     3
   /  \
  9   20
     /  \
   15    7

Example 2:
Input: preorder = [-1], inorder = [-1],  Output: [-1]

Example 3:
Input: preorder = [1, 2, 3], inorder = [2, 1, 3],  Output: [1, 2, 3]

    1
   / \
  2   3
"""

"""
We know the first item of the preorder list is going to be the root. Looking at the inorder list, we can see 
that it splits into the left and right hand side of the trees from the given node. Thus we construct the tree in a
preorder fashion (node, left, right), splitting the inorder list based on where the given value is found. If the 
inorder list is empty that means that no more nodes are to be assigned, so we return. We can avoid having to create
slices of the inorder list by passing indices to search in (the list.index() method is very helpful for this).
"""


from shared import TreeNode


def build_tree(preorder, inorder):

    preorder_idx = 0

    def helper(low, high):
        nonlocal preorder_idx
        if low == high:
            return None
        value = preorder[preorder_idx]
        node = TreeNode(value)
        inorder_idx = inorder.index(value, low, high)
        preorder_idx += 1
        node.left = helper(low, inorder_idx)
        node.right = helper(inorder_idx + 1, high)
        return node

    return helper(0, len(inorder))


tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]) == tree

tree = TreeNode(-1)
assert build_tree([-1], [-1]) == tree

tree = TreeNode(1, TreeNode(2), TreeNode(3))
assert build_tree([1, 2, 3], [2, 1, 3]) == tree
