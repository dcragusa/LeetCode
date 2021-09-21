"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

class Node:
    val: int
    left: Optional[Node]
    right : Optional[Node]
    next: Optional[Node]

Populate each next variable to point to its next right node. If there is no next right node, the next variable should
be set to None. Initially, all next variables are set to None.


Example 1:
Input: root = [1, 2, 3, 4, 5, 6, 7],  Output: [1, #, 2, 3, #, 4, 5, 6, 7, #]

         1                  1 -> #
       /   \              /   \
     2      3           2  ->  3 -> #
   /  \    / \        /  \    /  \
  4   5   6   7      4 -> 5->6 -> 7 -> #

Explanation: Given the above perfect binary tree (left), your function should populate each next pointer to
point to its next right node, (right tree). The serialized output is in level order as connected by the
next pointers, with '#' signifying the end of each level.

Example 2:
Input: root = [],  Output: []
"""

"""
Solving this is simple - we utilise breadth-first traversal with a queue, iterating from right to left. We save both
the depth and node to the queue, so we know whether the 'next node' is of the same level. If not, this must be the 
rightmost node of a level, so we reset the next node to be the current node.
"""

from collections import deque
from shared import list_to_tree


def connect(root):

    next_node = (-1, None)
    queue = deque([(0, root)])
    while queue:
        depth, node = queue.popleft()
        if node is None:
            continue
        if depth != next_node[0]:
            next_node = depth, node
        elif next_node[1]:
            node.next = next_node[1]
            next_node = depth, node
        queue.append((depth + 1, node.right))
        queue.append((depth + 1, node.left))

    return root


connect(list_to_tree([1, 2, 3, 4, 5, 6, 7]))
