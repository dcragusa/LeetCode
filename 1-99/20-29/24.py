"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

"""
Firstly we swap the first two elements. We then iterate across the list, copying the nodes into temporary variables
so as not to mess the order, and reassigning the next params as needed.
From current -> current.next -> current.next.next -> current.next.next.next, we need to swap the central two elements.
We end up with current -> current.next.next -> current.next -> current.next.next.next, then we just move current 
two elements along and repeat.
"""

from shared import python_list_to_linked_list, linked_list_to_python_list


def swap_pairs(head):
    if not head or not head.next:
        return head
    current = head
    head = head.next
    current.next = current.next.next
    head.next = current
    while current and current.next and current.next.next:
        n = current.next
        n_n = n.next
        n_n_n = n_n.next
        n.next = n_n_n
        n_n.next = n
        current.next = n_n
        current = current.next.next
    return head


assert linked_list_to_python_list(swap_pairs(None)) == []

head = python_list_to_linked_list([1])
assert linked_list_to_python_list(swap_pairs(head)) == [1]

head = python_list_to_linked_list([1, 2])
assert linked_list_to_python_list(swap_pairs(head)) == [2, 1]

head = python_list_to_linked_list([1, 2, 3])
assert linked_list_to_python_list(swap_pairs(head)) == [2, 1, 3]

head = python_list_to_linked_list([1, 2, 3, 4, 5, 6])
assert linked_list_to_python_list(swap_pairs(head)) == [2, 1, 4, 3, 6, 5]

head = python_list_to_linked_list([1, 2, 3, 4])
assert linked_list_to_python_list(swap_pairs(head)) == [2, 1, 4, 3]
