"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output: [[1, None, 3, 2],
         [3, 2, None, 1],
         [3, 1, None, None, 2],
         [2, 1, 3],
         [1, None, 2, None, 3]]
Explanation:
The above output corresponds to the 5 unique BST's shown below:
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

"""
We recursively generate left and right halves of the tree for each root node in the range[1, n].
"""


from shared import TreeNode
from itertools import product
from functools import lru_cache


def generate_trees(n):
    if not n:
        return []

    @lru_cache()
    def recur(left, right):
        result = []
        for i in range(left, right+1):
            for l, r in product(recur(left, i-1), recur(i+1, right)):
                node = TreeNode(i)
                node.left = l
                node.right = r
                result.append(node)
        return result if result else [None]

    return recur(1, n)
