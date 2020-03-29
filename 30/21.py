"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4, Output: 1->1->2->3->4->4
"""

"""
We take the lowest value as the head of the new linked list, then go through the two lists, adding the lowest value
to the new linked list as we go.
"""

from shared import python_list_to_linked_list, linked_list_to_python_list


def merge_two_lists(list1, list2):
    if not list1 or not list2:
        return list1 or list2
    head = current = None
    while list1 and list2:
        if (list1 and not list2) or (list1 and list2 and list1.val <= list2.val):
            if head is None:
                head = current = list1
            else:
                current.next = list1
                current = current.next
            list1 = list1.next
        else:
            if head is None:
                head = current = list2
            else:
                current.next = list2
                current = current.next
            list2 = list2.next
    current.next = list1 or list2
    return head


one = python_list_to_linked_list([1, 2, 4])
two = python_list_to_linked_list([1, 3, 4])
assert linked_list_to_python_list(merge_two_lists(one, two)) == [1, 1, 2, 3, 4, 4]

one = python_list_to_linked_list([1, 3, 4])
two = python_list_to_linked_list([2])
assert linked_list_to_python_list(merge_two_lists(one, two)) == [1, 2, 3, 4]

one = python_list_to_linked_list([2])
assert linked_list_to_python_list(merge_two_lists(one, None)) == [2]
