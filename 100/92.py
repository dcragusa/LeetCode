"""
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4,  Output: 1->4->3->2->5->NULL
"""

"""
We obtain the first node we are reversing (current), along with the node before that (reversal_head). Then we iterate
along the nodes we are reversing, adding them to a stack. Finally, we go back down the stack, adding the last node to
reversal_head and advancing reversal_head. (If m is 1, that means the head itself is being reversed, so reversal_head
is the first node popped off the stack). Finally, we set the next node to be the continuation of the original list.
"""

from shared import python_list_to_linked_list, linked_list_to_python_list


def reverse_between(head, m, n):

    current = head
    if m == 1:
        reversal_head = None
    else:
        for _ in range(m-2):
            current = current.next
        reversal_head = current
        current = current.next

    stack = []
    for _ in range(n-m+1):
        stack.append(current)
        current = current.next

    while stack:
        if reversal_head:
            reversal_head.next = stack.pop()
            reversal_head = reversal_head.next
        else:
            reversal_head = stack.pop()
            head = reversal_head
    reversal_head.next = current

    return head


assert linked_list_to_python_list(reverse_between(python_list_to_linked_list([1, 2, 3, 4, 5]), 4, 5)) == [1, 2, 3, 5, 4]
assert linked_list_to_python_list(reverse_between(python_list_to_linked_list([1, 2, 3, 4, 5]), 1, 5)) == [5, 4, 3, 2, 1]
assert linked_list_to_python_list(reverse_between(python_list_to_linked_list([1, 2, 3, 4, 5]), 1, 2)) == [2, 1, 3, 4, 5]
assert linked_list_to_python_list(reverse_between(python_list_to_linked_list([1, 2, 3, 4, 5]), 2, 4)) == [1, 4, 3, 2, 5]
