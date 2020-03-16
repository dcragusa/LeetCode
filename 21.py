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


class ListNode:
    def __init__(self, x):
        self.val, self.next = x, None


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


def linked_list_to_python_list(head):
    python_list = []
    node = head
    while node:
        python_list.append(node.val)
        node = node.next
    return python_list


one_1, two_1, four_1 = ListNode(1), ListNode(2), ListNode(4)
one_1.next, two_1.next = two_1, four_1
one_2, three_2, four_2 = ListNode(1), ListNode(3), ListNode(4)
one_2.next, three_2.next = three_2, four_2
assert linked_list_to_python_list(merge_two_lists(one_1, one_2)) == [1, 1, 2, 3, 4, 4]

two_1 = ListNode(2)
one_2, three_2, four_2 = ListNode(1), ListNode(3), ListNode(4)
one_2.next, three_2.next = three_2, four_2
assert linked_list_to_python_list(merge_two_lists(two_1, one_2)) == [1, 2, 3, 4]

two_1 = ListNode(2)
assert linked_list_to_python_list(merge_two_lists(two_1, None)) == [2]
