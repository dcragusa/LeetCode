"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2,  Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4,  Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

"""
Firstly we traverse the entire list for several reasons: to get a map of indices to nodes for later O(1) access, 
to establish the length of the list, and to reach the last element. We set k = (k mod length), in case k is greater 
than the length of the list. Then we have to set the next of the last element to the first one, set the head as the 
(length-k)th item of the list, and set the previous item to that to have a null next.
If we wish to stay in O(1) space constraints, we can omit creating the map of indices and simply traverse the list 
again until we get to the (length-k-1)th item, and then we perform the same procedures as before.
"""


from itertools import count
from shared import linked_list_to_python_list, python_list_to_linked_list


def rotate_right(head, k):
    if not head or not k:
        return head

    idxs, current = {}, head
    for i in count():
        idxs[i] = current
        if not current.next:
            break
        current = current.next

    n = len(idxs)
    k %= n
    if not k:
        return head

    idxs[n-1].next = idxs[0]
    idxs[n-k-1].next = None
    return idxs[n-k]


head = python_list_to_linked_list([])
assert linked_list_to_python_list(rotate_right(head, 5)) == []

head = python_list_to_linked_list([1])
assert linked_list_to_python_list(rotate_right(head, 5)) == [1]

head = python_list_to_linked_list([1, 2])
assert linked_list_to_python_list(rotate_right(head, 2)) == [1, 2]

head = python_list_to_linked_list([1, 2, 3, 4, 5])
assert linked_list_to_python_list(rotate_right(head, 0)) == [1, 2, 3, 4, 5]

head = python_list_to_linked_list([1, 2, 3, 4, 5])
assert linked_list_to_python_list(rotate_right(head, 2)) == [4, 5, 1, 2, 3]

head = python_list_to_linked_list([0, 1, 2])
assert linked_list_to_python_list(rotate_right(head, 4)) == [2, 0, 1]
