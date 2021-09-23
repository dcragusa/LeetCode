"""
Given the root of a binary tree and an integer `target_sum`, return `True` if the tree has a root-to-leaf path
such that adding up all the values along the path equals `target_sum`. A leaf is a node with no children.

Example 1:
Input: root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], target_sum = 22
Output: [[5, 4, 11, 2], [5, 8, 4, 5]]

         5
       /  \
      4    8
     /    / \
    11   13  4
   / \      / \
  7   2    5   1

Example 2:
Input: root = [1, 2, 3], target_sum = 5,  Output: []

    1
   / \
  2   3

Example 3:
Input: root = [1, 2], target_sum = 0,  Output: []

    1
   /
  2
"""

"""
Similar to 112, except we keep track of the path as we recur down the tree, and append it to a list of results
when we find a matching leaf node.
"""

from shared import list_to_tree


def path_sum(root, target_sum):
    results = []

    def helper(node, path, target_sum):
        if node is None:
            return
        if node.left is None and node.right is None and node.val == target_sum:
            results.append(path + [node.val])
        if node.left:
            helper(node.left, path + [node.val], target_sum - node.val)
        if node.right:
            helper(node.right, path + [node.val], target_sum - node.val)

    helper(root, [], target_sum)
    return results


assert path_sum(list_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]
assert path_sum(list_to_tree([1, 2, 3]), 5) == []
assert path_sum(list_to_tree([1, 2]), 0) == []
