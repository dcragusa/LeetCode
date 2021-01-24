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

from shared import ListNode, python_list_to_linked_list, linked_list_to_python_list


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


one = python_list_to_linked_list([2, 4, 3])
two = python_list_to_linked_list([5, 6, 4])
assert linked_list_to_python_list(add_two_numbers(one, two)) == [7, 0, 8]

one = python_list_to_linked_list([1, 2, 3])
two = python_list_to_linked_list([0])
assert linked_list_to_python_list(add_two_numbers(one, two)) == [1, 2, 3]

one = python_list_to_linked_list([1, 1, 9])
two = python_list_to_linked_list([1, 1, 9])
assert linked_list_to_python_list(add_two_numbers(one, two)) == [2, 2, 8, 1]
