"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the
original list. Return the linked list sorted as well.

Example 1:
Input: 1->2->3->3->4->4->5,  Output: 1->2->5

Example 2:
Input: 1->1->1->2->3,  Output: 2->3
"""

"""
We go through the linked list, keeping track of the current node and last unique node. We check if the next node's 
value is equal to the current one. If it is, a 'repeating' flag is set. When we find a different value, if there is no 
repeating flag, we simply update the last unique node to be the current one. If the repeating flag is set, this is the
first unique value after a set of repeated values, so we clear the flag and update the next node of the last unique 
node to be the current node. If there is no last unique node, it means the head itself had repeating values, so we 
update the head to be the current node instead. We return the head after iterating through the whole list.
"""


from shared import python_list_to_linked_list, linked_list_to_python_list


def delete_duplicates(head):
    last_unique_node = None
    current_node = head
    repeating = False
    while current_node:
        next_val = current_node.next.val if current_node.next else None
        if next_val != current_node.val:
            if repeating:
                if last_unique_node:
                    last_unique_node.next = current_node.next
                else:
                    head = current_node.next
                repeating = False
            else:
                last_unique_node = current_node
        else:
            repeating = True
        current_node = current_node.next
    return head


assert linked_list_to_python_list(delete_duplicates(python_list_to_linked_list([]))) == []
assert linked_list_to_python_list(delete_duplicates(python_list_to_linked_list([1, 1]))) == []
assert linked_list_to_python_list(delete_duplicates(python_list_to_linked_list([1, 2, 3, 3, 4, 4, 5]))) == [1, 2, 5]
assert linked_list_to_python_list(delete_duplicates(python_list_to_linked_list([1, 1, 1, 2, 3]))) == [2, 3]
assert linked_list_to_python_list(delete_duplicates(python_list_to_linked_list([1, 1, 1, 2, 3, 3]))) == [2]
