"""
Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right child pointer points to the next node
  in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1, 2, 5, 3, 4, None, 6],  Output: [1, None, 2, None, 3, None, 4, None, 5, None, 6]

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

from shared import list_to_tree, TreeNode


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


tree = list_to_tree([1, 2, 5, 3, 4, None, 6])
flatten(tree)
assert tree == list_to_tree([1, None, 2, None, 3, None, 4, None, 5, None, 6])

tree = list_to_tree([1, 2, 7, 3, 4, None, 8, None, None, 5, 6])
flatten(tree)
assert tree == list_to_tree([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])

tree = list_to_tree([])
flatten(tree)
assert tree == list_to_tree([])

tree = list_to_tree([0])
flatten(tree)
assert tree == list_to_tree([0])
