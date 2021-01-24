"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or
equal to x. You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3,  Output: 1->2->2->4->3->5
"""

"""
We iterate across the linked list. If we find a value greater or equal to x, we move it to a separate linked list.
After we have exhausted the linked list, we attach the other linked list to the end of the original one, thus moving
all values greater or equal to x to the end whilst preserving relative order.
"""


from shared import python_list_to_linked_list, linked_list_to_python_list


def partition(head, x):
    other_head = other_current = None
    current = head
    while current:
        if head.val >= x:
            # if the head itself is >= x, we must move the node to the other list and update head
            if not other_head:
                other_head = other_current = head
            else:
                other_current.next = head
                other_current = other_current.next
            head = current = current.next
            other_current.next = None
        elif not current.next:
            # we have reached the end of the list: attach other head to list and return
            current.next = other_head
            return head
        elif current.next.val >= x:
            # the next value is >= x, move the next node to the other list and update the current next
            if not other_head:
                other_head = other_current = current.next
            else:
                other_current.next = current.next
                other_current = other_current.next
            current.next = current.next.next
            other_current.next = None
        else:
            # next node is < x, update current node
            current = current.next
    # if we reach here, every node was >= x. Hence we just have to return other head as it contains all nodes.
    return other_head


assert linked_list_to_python_list(partition(python_list_to_linked_list([4, 1]), 2)) == [1, 4]
assert linked_list_to_python_list(partition(python_list_to_linked_list([4, 3]), 2)) == [4, 3]
assert linked_list_to_python_list(partition(python_list_to_linked_list([1, 4, 3, 2, 5, 2]), 3)) == [1, 2, 2, 4, 3, 5]
assert linked_list_to_python_list(partition(python_list_to_linked_list([1, 2, 3, 4, 5]), 6)) == [1, 2, 3, 4, 5]
