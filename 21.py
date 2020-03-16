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

from shared import ListNode, linked_list_to_python_list


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


one1, one2, one3 = ListNode(1), ListNode(2), ListNode(4)
one1.next, one2.next = one2, one3
two1, two2, two3 = ListNode(1), ListNode(3), ListNode(4)
two1.next, two2.next = two2, two3
assert linked_list_to_python_list(merge_two_lists(one1, two1)) == [1, 1, 2, 3, 4, 4]


one1, one2, one3 = ListNode(1), ListNode(3), ListNode(4)
one1.next, one2.next = one2, one3
two1 = ListNode(2)
assert linked_list_to_python_list(merge_two_lists(one1, two1)) == [1, 2, 3, 4]

one1 = ListNode(2)
assert linked_list_to_python_list(merge_two_lists(one1, None)) == [2]
