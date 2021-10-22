"""
Given the root of a complete binary tree, return the number of the nodes in the tree. Every level, except possibly the
last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It
can have between 1 and 2h nodes inclusive at the last level h. Your algorithm must run in less than O(n) time.

Example 1:
Input: root = [1, 2, 3, 4, 5, 6],  Output: 6

        1
      /   \
    2      3
   / \    /
  4   5  6

Example 2:
Input: root = [],  Output: 0

Example 3:
Input: root = [1],  Output: 1
"""

"""
We can solve this in lesser than O(n) time by examining the depth of the left and right side of the tree. If the depths
are equal, the tree is a perfect binary tree (last level has all leaf nodes present). In this case, it is easy to
calculate the number of nodes in the tree by powers of 2. If the left depth is bigger than right depth, we apply this
reasoning recursively to the left and right nodes of the root. At each split we are guaranteed that either the left or
right subtree is perfect (at which point we stop recursion). Hence, seeing as we do not examine all nodes, the time
complexity is better than O(n).
"""

from shared import list_to_tree


def count_nodes(root):

    if not root:
        return 0

    def find_depth(node, left_direction):
        d = 0
        while node:
            d += 1
            node = node.left if left_direction else node.right
        return d

    left_depth = find_depth(root.left, True)
    right_depth = find_depth(root.right, False)

    if left_depth == right_depth:
        return 2 ** (left_depth+1) - 1
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)


assert count_nodes(list_to_tree(list(range(6)))) == 6
assert count_nodes(list_to_tree([])) == 0
assert count_nodes(list_to_tree([1])) == 1
assert count_nodes(list_to_tree(list(range(31)))) == 31
