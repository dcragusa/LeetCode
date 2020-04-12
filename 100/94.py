"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: The recursive solution is trivial, could you do it iteratively?
"""

"""
As the problem states, the recursive solution is trivial.
For the iterative solution, we first try and go down the left as far as we can, keeping a history of nodes so we can 
backtrack. Once we have found a node with no left children, we add that node to the results and attempt to go down to
the right. If there are right children, we add the current node to the results and try to go down the left again
(without adding the current node to the history, so we skip it on the way back up).  If there are no right children,
we have reached the end of the tree and result the list of node values. Some error checking is involved to see whether 
the current node has already been added to the results on direction change or tree exhaustion.
"""


from shared import TreeNode


def inorder_traversal_recursive(root):
    results = []

    def recur(node):
        if node is None:
            return
        recur(node.left)
        results.append(node.val)
        recur(node.right)

    recur(root)
    return results


def inorder_traversal_iterative(root):
    results = []
    direction = 'l'
    node = root
    node_history = []
    while node:
        if direction == 'l':
            if node.left:
                node_history.append(node)
                node = node.left
            else:
                results.append(node)
                direction = 'r'
        elif direction == 'r':
            if node.right:
                if not results or results[-1] != node:
                    results.append(node)
                node = node.right
                direction = 'l'
            else:
                if not results or results[-1] != node:
                    results.append(node)
                if not node_history:
                    return [result.val for result in results]
                node = node_history.pop()


# example
tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
assert inorder_traversal_recursive(tree) == inorder_traversal_iterative(tree) == [1, 3, 2]

#      1
#    /   \
#   2     5
#  / \   / \
# 3   4 6   7
tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7)))
assert inorder_traversal_recursive(tree) == inorder_traversal_iterative(tree) == [3, 2, 4, 1, 6, 5, 7]
