"""
Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node. Note: A leaf is a node with no children.

Example 1:
Input: root = [3, 9, 20, null, null, 15, 7],  Output: 2

    3
   / \
  9  20
    /  \
   15   7

Example 2:
Input: root = [1, 2, 2, 3, 3, null, null, 4, 4],  Output: 2

        1
       / \
      2   2
     / \
    3   3
   / \
  4   4

Example 3:
Input: root = [1,2,null,3,null,4,null,5],  Output: 5

          1
         /
        2
       /
      3
     /
    4
   /
  5
"""

"""
Since we are trying to find the minimum depth, a breadth-first search is more appropriate here. This is implemented
by a deque (for fast pops on the left end). As soon as we find a leaf node (both children are None), return the depth.
"""

from shared import TreeNode
from collections import deque


def min_depth(root):

    if root is None:
        return 0

    queue = deque([(root, 1)])
    while queue:
        node, level = queue.popleft()
        if not node.left and not node.right:
            return level
        if node.left:
            queue.append((node.left, level+1))
        if node.right:
            queue.append((node.right, level+1))


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert min_depth(root) == 2

root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
assert min_depth(root) == 2

root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))
assert min_depth(root) == 5

root = None
assert min_depth(root) == 0
