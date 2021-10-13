"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1, 2, 3, 4, 5],  Output: [5, 4, 3, 2, 1]

Example 2:
Input: head = [1, 2],  Output: [2, 1]

Example 3:
Input: head = [],  Output: []
"""

"""
Pretty simple: we set up a previous node initialised to None. We then iterate across the linked list, keeping track of
next node. We then set the next pointer to point to the previous node and update the head and previous node, moving on
to the previously tracked next node. When we reach the end, head will be None so we return the previous node.
"""

from shared import linked_list_to_python_list, python_list_to_linked_list


def reverse_list(head):
    prev_node = None
    while head:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node
    return prev_node


assert linked_list_to_python_list(reverse_list(python_list_to_linked_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
assert linked_list_to_python_list(reverse_list(python_list_to_linked_list([1, 2]))) == [2, 1]
assert linked_list_to_python_list(reverse_list(python_list_to_linked_list([]))) == []
assert linked_list_to_python_list(reverse_list(python_list_to_linked_list([1]))) == [1]
