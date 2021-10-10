"""
Given the root of a binary tree, imagine yourself standing on the right side of it and return the values of the nodes
you can see ordered from top to bottom.

Example 1:
Input: root = [1, 2, 3, None, 5, None, 4],  Output: [1, 3, 4]

    1
   / \
  2   3
   \   \
    5   4

Example 1:
Input: root = [1, 2, 3, None, 5],  Output: [1, 3, 5]

    1
   / \
  2   3
  \
   5

Example 3:
Input: root = [1, none, 3],  Output: [1, 3]

  1
   \
    3

Example 4:
Input: root = [],  Output: []
"""

"""
We can implement this in reverse pre-order traversal (node, right, left), keeping track of the level of the tree we
are in. We only add values to the result array if the length of the result array is equal to the level (i.e., only one
value per level). Because we traverse the tree right-node-first, we are guaranteed the view from the right.
"""

from shared import list_to_tree


def right_side_view(root):

    results = []

    def helper(node, level):
        if not node:
            return
        if len(results) == level:
            results.append(node.val)
        helper(node.right, level + 1)
        helper(node.left, level + 1)

    helper(root, 0)
    return results


assert right_side_view(list_to_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
assert right_side_view(list_to_tree([1, 2, 3, None, 5])) == [1, 3, 5]
assert right_side_view(list_to_tree([1, None, 3])) == [1, 3]
assert right_side_view(list_to_tree([])) == []
