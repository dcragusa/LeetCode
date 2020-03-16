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


class ListNode:
    def __init__(self, x):
        self.val, self.next = x, None

    def __repr__(self):
        return f'{self.val}'


def swap_pairs(head):
    if not head:
        return None
    if not head.next:
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


def linked_list_to_python_list(head):
    python_list = []
    node = head
    while node:
        python_list.append(node.val)
        node = node.next
    return python_list


assert linked_list_to_python_list(swap_pairs(None)) == []

assert linked_list_to_python_list(swap_pairs(ListNode(1))) == [1]

one, two = ListNode(1), ListNode(2)
one.next = two
assert linked_list_to_python_list(swap_pairs(one)) == [2, 1]

one, two, three = ListNode(1), ListNode(2), ListNode(3)
one.next, two.next = two, three
assert linked_list_to_python_list(swap_pairs(one)) == [2, 1, 3]

one, two, three, four, five, six = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6)
one.next, two.next, three.next, four.next, five.next = two, three, four, five, six
assert linked_list_to_python_list(swap_pairs(one)) == [2, 1, 4, 3, 6, 5]

one, two, three, four = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
one.next, two.next, three.next = two, three, four
assert linked_list_to_python_list(swap_pairs(one)) == [2, 1, 4, 3]
