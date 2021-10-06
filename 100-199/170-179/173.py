"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST).
- BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of
  the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
- boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise
  returns false.
- int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the
smallest element in the BST. You may assume that next() calls will always be valid. That is, there will be at least
a next number in the in-order traversal when next() is called.

Example 1:

    7
   / \
  3  15
    /  \
   9   20

Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
"""

"""
We can either implement an iterative solution, similar to problem 94's iterative approach, or simply precompute
the in-order traversal of the tree and return next and hasNext based on a list iteration.
"""

from shared import list_to_tree


# class BSTIterator:
#
#     def __init__(self, root):
#         self.node = root
#         self.stack = []
#         self.left = bool(self.node and self.node.left)
#         self.last_node = None
#
#     def hasNext(self):
#         if not self.node:
#             return False
#         if not self.last_node:
#             return True
#         if self.left and self.node.left:
#             return True
#         if not self.left and self.node.right:
#             return True
#         if not self.left and self.stack:
#             return True
#         return False
#
#     def next(self):
#         while self.node:
#             if self.left:
#                 if self.node.left:
#                     self.stack.append(self.node)
#                     self.node = self.node.left
#                 else:
#                     self.left = False
#                     self.last_node = self.node
#                     return self.node.val
#             else:
#                 if self.node.right:
#                     if not self.last_node or self.last_node is not self.node:
#                         self.last_node = self.node
#                         return self.node.val
#                     self.node = self.node.right
#                     self.left = True
#                 else:
#                     if not self.last_node or self.last_node is not self.node:
#                         self.last_node = self.node
#                         return self.node.val
#                     self.node = self.stack.pop()


class BSTIterator:

    def __init__(self, root):
        self.node = root
        self.index = 0
        self.vals = []
        self.populate(self.node)

    def populate(self, node):
        if node is None:
            return
        self.populate(node.left)
        self.vals.append(node.val)
        self.populate(node.right)

    def hasNext(self):
        return self.index < len(self.vals)

    def next(self):
        val = self.vals[self.index]
        self.index += 1
        return val


#     7
#    / \
#   3  15
#     /  \
#    9   20
iterator = BSTIterator(list_to_tree([7, 3, 15, None, None, 9, 20]))
assert iterator.next() == 3
assert iterator.next() == 7
assert iterator.hasNext() is True
assert iterator.next() == 9
assert iterator.hasNext() is True
assert iterator.next() == 15
assert iterator.hasNext() is True
assert iterator.next() == 20
assert iterator.hasNext() is False


#       1
#      /  \
#     2    2
#    /\    /\
#   3  4  4  3
iterator = BSTIterator(list_to_tree([1, 2, 2, 3, 4, 4, 3]))
assert iterator.next() == 3
assert iterator.next() == 2
assert iterator.next() == 4
assert iterator.next() == 1
assert iterator.next() == 4
assert iterator.next() == 2
assert iterator.hasNext() is True
assert iterator.next() == 3
assert iterator.hasNext() is False


#   1
#    \
#     2
iterator = BSTIterator(list_to_tree([1, None, 2]))
assert iterator.hasNext() is True
assert iterator.next() == 1
assert iterator.hasNext() is True
assert iterator.next() == 2
assert iterator.hasNext() is False


#     1
#    /
#   2
iterator = BSTIterator(list_to_tree([1, 2]))
assert iterator.hasNext() is True
assert iterator.next() == 2
assert iterator.hasNext() is True
assert iterator.next() == 1
assert iterator.hasNext() is False


iterator = BSTIterator(list_to_tree([1]))
assert iterator.hasNext() is True
assert iterator.next() == 1
assert iterator.hasNext() is False


iterator = BSTIterator(list_to_tree([]))
assert iterator.hasNext() is False
