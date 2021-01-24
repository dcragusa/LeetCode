"""
Given a sorted linked list, delete all duplicates such that each element appears only once.

Example 1:
Input: 1->1->2,  Output: 1->2

Example 2:
Input: 1->1->2->3->3,  Output: 1->2->3
"""

"""
Fairly simple, we skip a node if it has the same value as the previous node.
"""


from shared import python_list_to_linked_list, linked_list_to_python_list


def delete_duplicates(head):
    prev_node, current_node = None, head
    while current_node:
        if prev_node and current_node.val == prev_node.val:
            prev_node.next = current_node.next
        else:
            prev_node = current_node
        current_node = current_node.next
    return head


assert linked_list_to_python_list(delete_duplicates(python_list_to_linked_list([]))) == []
assert linked_list_to_python_list(delete_duplicates(python_list_to_linked_list([1]))) == [1]
assert linked_list_to_python_list(delete_duplicates(python_list_to_linked_list([1, 1]))) == [1]
assert linked_list_to_python_list(delete_duplicates(python_list_to_linked_list([1, 1, 1]))) == [1]
assert linked_list_to_python_list(delete_duplicates(python_list_to_linked_list([1, 1, 2]))) == [1, 2]
assert linked_list_to_python_list(delete_duplicates(python_list_to_linked_list([1, 1, 2, 2, 3, 3]))) == [1, 2, 3]
