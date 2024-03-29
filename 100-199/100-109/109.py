"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced
BST. For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
of every node never differ by more than 1.

Example 1:
Input: head = [-10, -3, 0, 5, 9],  Output: [0, -3, 9, -10, None, 5]  (or [0, -10, 5, None, -3, None, 9])

        0               0
       / \             / \
     -3   9    or    -10  5
    /    /             \   \
  -10   5              -3   9

Example 2:
Input: nums = [1, 3],  Output: [3, 1]  (or [1, 3])

    3        1
   /    or    \
  1            3

Example 3:
Input: head = [],  Output: []

Example 4:
Input: head = [0],  Output: [0]
"""

"""
Identical to 108 except we read out the linked list into a normal Python list beforehand.
"""

from shared import TreeNode, python_list_to_linked_list, list_to_tree


def sorted_linked_list_to_bst(head):
    nums = []
    while head is not None:
        nums.append(head.val)
        head = head.next

    def helper(low, high):
        if low == high:
            return
        mid = (low + high) // 2
        return TreeNode(nums[mid], helper(low, mid), helper(mid + 1, high))

    return helper(0, len(nums))


linked_list = python_list_to_linked_list([-10, -3, 0, 5, 9])
assert sorted_linked_list_to_bst(linked_list) == list_to_tree([0, -3, 9, -10, None, 5])
assert sorted_linked_list_to_bst(python_list_to_linked_list([1, 3])) == list_to_tree([3, 1])
assert sorted_linked_list_to_bst(python_list_to_linked_list([])) == list_to_tree([])
assert sorted_linked_list_to_bst(python_list_to_linked_list([0])) == list_to_tree([0])
