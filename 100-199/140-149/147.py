"""
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
The steps of the insertion sort algorithm:
- Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
- At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the
  sorted list and inserts it there.
- It repeats until no input elements remain.

Example 1:
Input: head = [4, 2, 1, 3],  Output: [1, 2, 3, 4]

Example 2:
Input: head = [-1, 5, 3, 4, 0],  Output: [-1, 0, 3, 4, 5]
"""

"""
Since we need to keep track of the previous and next nodes after insertion, we add a dummy head at the start of the
linked list to avoid special-casing the head node every time. We then iterate across the linked list. For each node, 
we examine the linked list up to that node for insertions (where the node value is smaller than the insertion value).
At the end we return the real head of the sorted list, skipping the dummy node we inserted.
"""

from shared import ListNode, linked_list_to_python_list, python_list_to_linked_list


def insertion_sort_list(head):
    if not head:
        return head
    head = ListNode(float('-inf'), head)
    prev_node, curr_node = head, head.next
    while curr_node:
        next_node = curr_node.next
        prev_insertion_node, insertion_node = head, head.next
        while insertion_node is not curr_node:
            if curr_node.val < insertion_node.val:
                prev_insertion_node.next = curr_node
                curr_node.next = insertion_node
                prev_node.next = next_node
                break
            prev_insertion_node, insertion_node = prev_insertion_node.next, insertion_node.next

        if insertion_node is curr_node:
            prev_node = prev_node.next
        curr_node = next_node

    return head.next


assert linked_list_to_python_list(insertion_sort_list(python_list_to_linked_list([4, 3, 2, 1]))) == [1, 2, 3, 4]
assert linked_list_to_python_list(insertion_sort_list(python_list_to_linked_list([1, 2, 4, 3]))) == [1, 2, 3, 4]
assert linked_list_to_python_list(insertion_sort_list(python_list_to_linked_list([4, 2, 1, 3]))) == [1, 2, 3, 4]
assert linked_list_to_python_list(insertion_sort_list(python_list_to_linked_list([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]

