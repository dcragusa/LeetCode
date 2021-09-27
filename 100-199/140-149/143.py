"""
You are given the head of a singly linked-list. The list can be represented as: L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form: L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1, 2, 3, 4],   Output: [1, 4, 2, 3]

Example 2:
Input: head = [1, 2, 3, 4, 5],   Output: [1, 5, 2, 4, 3]
"""

"""
We read out the linked list to a Python list, then maintain two pointers to the start and end of the list, reassigning
next pointers and counting inwards. When the start and end pointers meet, we know that is the end of the resulting list
so we assign the next pointer to None to terminate.
"""

from shared import python_list_to_linked_list, linked_list_to_python_list


def reorder_list(head):
    node_list = []
    while head:
        node_list.append(head)
        head = head.next
    start_idx, end_idx = 0, len(node_list) - 1
    while start_idx != end_idx:
        node_list[start_idx].next = node_list[end_idx]
        start_idx += 1
        if start_idx != end_idx:
            node_list[end_idx].next = node_list[start_idx]
            end_idx -= 1
    node_list[start_idx].next = None
    return node_list[0]


assert linked_list_to_python_list(reorder_list(python_list_to_linked_list([1, 2, 3, 4]))) == [1, 4, 2, 3]
assert linked_list_to_python_list(reorder_list(python_list_to_linked_list([1, 2, 3, 4, 5]))) == [1, 5, 2, 4, 3]
