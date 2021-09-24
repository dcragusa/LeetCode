"""
You are given the root of a binary tree containing digits from 0 to 9 only. Each root-to-leaf path in the tree
represents a number. For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123. Return the total
sum of all root-to-leaf numbers. A leaf node is a node with no children.

Example 1:
Input: root = [1, 2, 3],  Output: 25
Explanation: 1->2 represents the number 12. 1->3 represents the number 13. sum = 12 + 13 = 25.

    1
   / \
  2   3

Example 2:
Input: root = [4, 9, 0, 5, 1],  Output: 1026
Explanation: 4->9->5 = 495. 4->9->1 = 491. 4->0 represents the number 40. sum = 495 + 491 + 40 = 1026.

      4
     / \
    9   0
   / \
  5   1
"""

"""
A naive solution might be to pass the path taken down until reaching a leaf node, but a better solution is to realise
that since going down a level shifts the number left, it is equivalent to multiplying by 10. Hence we just have to keep
multiplying by 10 as we go down the path, summing to the total when we reach a leaf node.
"""

from shared import list_to_tree


def sum_numbers(root):
    total_sum = 0

    def helper(node, path_sum):
        nonlocal total_sum
        if node is None:
            return
        path_sum += node.val
        if not node.left and not node.right:
            total_sum += path_sum
            return
        helper(node.left, path_sum * 10)
        helper(node.right, path_sum * 10)

    helper(root, 0)
    return total_sum


assert sum_numbers(list_to_tree([1, 2, 3])) == 25
assert sum_numbers(list_to_tree([4, 9, 0, 5, 1])) == 1026
