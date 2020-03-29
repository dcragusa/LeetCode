"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note: Given n will always be valid.
Follow up: Could you do this in one pass?
"""

"""
We keep a pointer to the head, and a pointer to the head minus the delay we need. If the head pointer is already None,
that means we are removing the first element so we set the head to the second element. If not, we iterate all the way
to the end of the linked list. The second pointer is now at the element prior to the one we are removing, so we 
simply change the next node to the node after the removed one (unless we are removing the last node, in which case
the next node is set directly to None).
"""

from shared import python_list_to_linked_list, linked_list_to_python_list


def remove_nth_from_end(head, n):

    first_pointer = head
    for _ in range(n):
        first_pointer = first_pointer.next
    second_pointer = head

    if not first_pointer:
        return second_pointer.next

    while first_pointer and first_pointer.next:
        first_pointer, second_pointer = first_pointer.next, second_pointer.next

    second_pointer.next = None if n == 1 else second_pointer.next.next

    return head


head = python_list_to_linked_list([1, 2, 3, 4, 5])
assert linked_list_to_python_list(remove_nth_from_end(head, 2)) == [1, 2, 3, 5]

head = python_list_to_linked_list([1])
assert linked_list_to_python_list(remove_nth_from_end(head, 1)) == []

head = python_list_to_linked_list([1, 2])
assert linked_list_to_python_list(remove_nth_from_end(head, 1)) == [1]

head = python_list_to_linked_list([1, 2])
assert linked_list_to_python_list(remove_nth_from_end(head, 2)) == [2]

head = python_list_to_linked_list([1, 2, 3])
assert linked_list_to_python_list(remove_nth_from_end(head, 2)) == [1, 3]

head = python_list_to_linked_list([1, 2, 3])
assert linked_list_to_python_list(remove_nth_from_end(head, 1)) == [1, 2]
