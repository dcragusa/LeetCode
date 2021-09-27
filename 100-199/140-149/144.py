"""
Given the root of a binary tree,  return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1, None, 2, 3],  Output: [1, 2, 3]

   1
    \
    2
   /
  3

Example 2:
Input: root = [],  Output: []

Example 3:
Input: root = [1],  Output: [1]

Example 4:
Input: root = [1, 2],  Output: [1, 2]

    1
   /
  2

Example 5:
Input: root = [1, None, 2],  Output: [1, 2]

  1
   \
    2
"""

from shared import list_to_tree


def preorder_traversal(root):
    results = []

    def helper(node):
        if node is None:
            return
        results.append(node.val)
        helper(node.left)
        helper(node.right)

    helper(root)
    return results


assert preorder_traversal(list_to_tree([1, None, 2, 3])) == [1, 2, 3]
assert preorder_traversal(list_to_tree([])) == []
assert preorder_traversal(list_to_tree([1])) == [1]
assert preorder_traversal(list_to_tree([1, 2])) == [1, 2]
assert preorder_traversal(list_to_tree([1, None, 2])) == [1, 2]
