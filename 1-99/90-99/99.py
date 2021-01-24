"""
Two elements of a binary search tree (BST) are swapped by mistake. Recover the tree without changing its structure.

Example 1:
Input: [1,3,null,null,2],  Output: [3,1,null,null,2]

  1        3
 /        /
3   ->   1
 \        \
  2        2

Example 2:
Input: [3,1,4,null,null,2],  Output: [2,1,4,null,null,3]

     3             2
    / \           / \
  1    4   ->   1    4
      /             /
     2             3
"""

"""
Here we perform an in-order traversal of the tree. As it is in order, any node that is less than the previous one
is out of order. The predecessor and wrong node are set to first and second nodes. If the swapped nodes are adjacent,
then we must only swap these two values. If they are not, there will be two pairs that need swapping - the first node 
of the first pair, and second node of the second pair.
"""

from shared import TreeNode


def recover_tree(root):

    first, second, predecessor = None, None, None

    def depth_first_search(node):
        nonlocal first, second, predecessor
        if not node:
            return

        depth_first_search(node.left)

        if predecessor and node.val < predecessor.val:
            second = node
            if not first:
                first = predecessor
        predecessor = node

        depth_first_search(node.right)

    depth_first_search(root)
    first.val, second.val = second.val, first.val



root = TreeNode(1, TreeNode(3, None, TreeNode(2)))
recover_tree(root)
assert root == TreeNode(3, TreeNode(1, None, TreeNode(2)))

root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
recover_tree(root)
assert root == TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3)))
