"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1, None, 2, 3],  Output: [3, 2, 1]

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
Input: root = [1, 2],  Output: [2, 1]

    1
   /
  2

Example 5:
Input: root = [1, None, 2],  Output: [2, 1]

  1
   \
    2
"""

"""
For postorder traversal, do left child, right child, value.
"""

from shared import list_to_tree


def postorder_traversal(root):
    results = []

    def helper(node):
        if node is None:
            return
        helper(node.left)
        helper(node.right)
        results.append(node.val)

    helper(root)
    return results


assert postorder_traversal(list_to_tree([1, None, 2, 3])) == [3, 2, 1]
assert postorder_traversal(list_to_tree([])) == []
assert postorder_traversal(list_to_tree([1])) == [1]
assert postorder_traversal(list_to_tree([1, 2])) == [2, 1]
assert postorder_traversal(list_to_tree([1, None, 2])) == [2, 1]

