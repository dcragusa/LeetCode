"""
Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right child pointer points to the next node
  in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1, 2, 5, 3, 4, null, 6],  Output: [1, null, 2, null, 3, null, 4, null, 5, null, 6]

                 1
                  \
                   2
      1             \
     / \             3
    2   5      ->     \
   / \   \             4
  3   4   6             \
                         5
                          \
                           6

Example 2:
Input: root = [],  Output: []

Example 3:
Input: root = [0],  Output: [0]
"""

from shared import TreeNode


def flatten(root):

    def find_last_left(node):
        while node and node.left:
            node = node.left
        return node

    def reorder(node):
        if node is None:
            return
        nonlocal last_left
        reorder(node.left)
        if node.right:
            last_left.left = node.right
            last_left = find_last_left(node.right)
            reorder(node.right)
            node.right = None

    last_left = find_last_left(root)
    reorder(root)
    node = root
    while node:
        node.right, node.left = node.left, None
        node = node.right


root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
flatten(root)
assert root == TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))))

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5), TreeNode(6))), TreeNode(7, None, TreeNode(8)))
flatten(root)
assert root == TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6, None, TreeNode(7, None, TreeNode(8))))))))

root = None
flatten(root)
assert root is None

root = TreeNode(0)
flatten(root)
assert root == TreeNode(0)

