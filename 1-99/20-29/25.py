"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5,
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

"""
First we obtain the node at the end of the first group. This is the node we will be returning. Then we go across the 
list, keeping track of the current tail and establishing the head of the next group. We then reverse that group, and
attach the current tail to the newly obtained head. We continue this process until the list is exhausted.
"""

from shared import python_list_to_linked_list, linked_list_to_python_list


def reverse_k_group(head, k):

    # obtain the first head
    next_head = head
    for _ in range(k-1):
        next_head = next_head.next
        if next_head is None:
            return head
    ret = next_head

    current = head
    while next_head:
        # keep track of the current tail
        tail, prev = current, None
        # reverse a group of k
        for _ in range(k):
            if next_head:
                next_head = next_head.next
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        # if there is a next head, we assign tail.next to that
        # if not, we assign it to the remainder of the current list
        tail.next = next_head or current

    return ret


head = python_list_to_linked_list([1, 2, 3, 4, 5])
assert linked_list_to_python_list(reverse_k_group(head, 2)) == [2, 1, 4, 3, 5]

head = python_list_to_linked_list([1, 2, 3, 4, 5])
assert linked_list_to_python_list(reverse_k_group(head, 3)) == [3, 2, 1, 4, 5]

head = python_list_to_linked_list([1, 2, 3, 4, 5])
assert linked_list_to_python_list(reverse_k_group(head, 4)) == [4, 3, 2, 1, 5]
