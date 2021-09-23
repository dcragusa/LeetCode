"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge
connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass
through the root. The path sum of a path is the sum of the node's values in the path. Given the root of a binary
tree, return the maximum path sum of any path.

Example 1:
Input: root = [1, 2, 3],  Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

    1
   / \
  2   3

Example 2:
Input: root = [-10, 9, 20, None, None, 15, 7],  Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

    -10
   /  \
  9   20
     /  \
    15   7
"""

"""
This is relatively easy to solve: the maximum path of a node is the maximum of the node's value or any combination
of sums of its left and right children. We pass the highest of node, node + left child, and node + right child
upwards (as only one path down can be chosen).
"""

from shared import list_to_tree


def max_path_sum(root):

    max_path_sum = float('-inf')

    def helper(node):
        nonlocal max_path_sum
        if not node:
            return 0
        left = helper(node.left)
        right = helper(node.right)
        max_path_sum = max(max_path_sum, node.val, node.val + left, node.val + right, node.val + left + right)
        return max(node.val, node.val + left, node.val + right)

    helper(root)
    return max_path_sum


assert max_path_sum(list_to_tree([1, 2, 3])) == 6
assert max_path_sum(list_to_tree([-10, 9, 20, None, None, 15, 7])) == 42
assert max_path_sum(list_to_tree([-3])) == -3
assert max_path_sum(list_to_tree([2, -1])) == 2
assert max_path_sum(list_to_tree([9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6])) == 16
