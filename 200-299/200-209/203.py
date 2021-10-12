"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that have node.val == val,
and return the new head.

Example 1:
Input: head = [1, 2, 6, 3, 4, 5, 6],  val = 6,  Output: [1, 2, 3, 4, 5]

Example 2:
Input: head = [],  val = 1,  Output: []

Example 3:
Input: head = [7, 7, 7, 7],  val = 7,  Output: []
"""

"""
We first set up a dummy head, which saves us from having to repeatedly check for the existence of head. We then iterate
over the linked list: if the next node is equal to val, we set the next node to be the one after that (and do not move
node, since the one after that could also be val). If the next node is not equal to val, we move to the next node.
Once we have finished iterating, we return the node after the dummy head.
"""

from shared import ListNode, python_list_to_linked_list, linked_list_to_python_list


def remove_elements(head, val):
    dummy = ListNode(None, head)
    node = dummy
    while node.next:
        if node.next.val == val:
            node.next = node.next.next
        else:
            node = node.next
    return dummy.next


assert linked_list_to_python_list(
    remove_elements(python_list_to_linked_list([1, 2, 6, 3, 4, 5, 6]), 6)
) == [1, 2, 3, 4, 5]
assert linked_list_to_python_list(remove_elements(python_list_to_linked_list([]), 1)) == []
assert linked_list_to_python_list(remove_elements(python_list_to_linked_list([7, 7, 7, 7]), 7)) == []
assert linked_list_to_python_list(remove_elements(python_list_to_linked_list([7, 7, 1, 2, 3]), 7)) == [1, 2, 3]
assert linked_list_to_python_list(remove_elements(python_list_to_linked_list([7, 7, 1, 2, 7, 3]), 7)) == [1, 2, 3]
assert linked_list_to_python_list(remove_elements(python_list_to_linked_list([1, 2, 2, 1]), 2)) == [1, 1]
