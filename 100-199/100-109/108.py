"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced
binary search tree. A height-balanced binary tree is a binary tree in which the depth of the two subtrees of
every node never differs by more than one.

Example 1:
Input: nums = [-10, -3, 0, 5, 9],  Output: [0, -3, 9, -10, null, 5]  (or [0, -10, 5, null, -3, null, 9])

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
"""

"""
The array is presorted, so to create a balanced tree we merely have to split the list in two halves of equal length
when creating the left and right sides recursively.
"""


from shared import TreeNode


def sorted_array_to_bst(nums):

    def helper(low, high):
        if low == high:
            return
        mid = (low + high) // 2
        return TreeNode(nums[mid], helper(low, mid), helper(mid + 1, high))

    return helper(0, len(nums))


tree = TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5)))
assert sorted_array_to_bst([-10, -3, 0, 5, 9]) == tree

tree = TreeNode(3, TreeNode(1))
assert sorted_array_to_bst([1, 3]) == tree
