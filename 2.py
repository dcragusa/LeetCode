"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

"""
We iterate across the linked list, summing and carrying. If one list is exhausted, we treat it as 0.
We add a new node on to the last node as we complete each digit, and make the last node the new node.
We only end when both lists are exhausted and there is no carry. Then we return the first node.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    first_node = last_node = None
    carry = 0

    while True:
        if l1 is None and l2 is None and carry == 0:
            return first_node

        v1 = 0 if l1 is None else l1.val
        v2 = 0 if l2 is None else l2.val

        sum_, carry = v1 + v2 + carry, 0
        if sum_ >= 10:
            sum_, carry = sum_ - 10, 1

        node = ListNode(sum_)
        if not first_node:
            first_node = node
        else:
            last_node.next = node
        last_node = node

        l1 = None if l1 is None else l1.next
        l2 = None if l2 is None else l2.next


def list_from_list_nodes(listnode):
    result = []
    while listnode is not None:
        result.append(listnode.val)
        listnode = listnode.next
    return result


one1, one2, one3 = ListNode(2), ListNode(4), ListNode(3)
one1.next = one2
one2.next = one3

two1, two2, two3 = ListNode(5), ListNode(6), ListNode(4)
two1.next = two2
two2.next = two3

r = add_two_numbers(one1, two1)
assert list_from_list_nodes(add_two_numbers(one1, two1)) == [7, 0, 8]

one1, one2, one3 = ListNode(1), ListNode(2), ListNode(3)
one1.next = one2
one2.next = one3

two1= ListNode(0)

r = add_two_numbers(one1, two1)
assert list_from_list_nodes(add_two_numbers(one1, two1)) == [1, 2, 3]

one1, one2, one3 = ListNode(1), ListNode(1), ListNode(9)
one1.next = one2
one2.next = one3

two1, two2, two3 = ListNode(1), ListNode(1), ListNode(9)
two1.next = two2
two2.next = two3

r = add_two_numbers(one1, two1)
assert list_from_list_nodes(add_two_numbers(one1, two1)) == [2, 2, 8, 1]
