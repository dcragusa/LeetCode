"""
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4, 2, 1, 3],  Output: [1, 2, 3, 4]

Example 2:
Input: head = [-1, 5, 3, 4, 0],  Output: [-1, 0, 3, 4, 5]

Example 3:
Input: head = [],  Output: []
"""

"""
There are several ways to do this: we can repeatedly push and pop off a heap (O(n log n) time, O(n) space), or simply
push onto an ordinary list and use Python's built in list sort, with the same big O complexity as the heap method. If 
we wish to run in O(n log n) time but only O(1) space, we must implement merge sort.
To do this, we recursively split up the linked list into two halves until each sub-list consists of at maximum one
element. We then combine these halves as we come up through the recursion, until we end up with a sorted list.
"""

import heapq
from operator import attrgetter
from shared import ListNode, linked_list_to_python_list, python_list_to_linked_list


# def sort_list_heap(head):
#     if head is None:
#         return head
#
#     heap = []
#     heapq.heapify(heap)
#     i = 0
#     while head:
#         heapq.heappush(heap, (head.val, i, head))
#         head = head.next
#         i += 1
#
#     head = node = heapq.heappop(heap)[1]
#     while heap:
#         popped = heapq.heappop(heap)[1]
#         node.next = popped
#         node = popped
#     node.next = None
#
#     return head


# def sort_list_python_sort(head):
#     if head is None:
#         return head
#
#     python_list = []
#
#     while head:
#         python_list.append(head)
#         head = head.next
#
#     python_list.sort(key=attrgetter('val'))
#
#     head = node = python_list[0]
#     for item in python_list[1:]:
#         node.next = item
#         node = item
#     node.next = None
#
#     return head


def sort_list(head):

    def get_mid(head):
        prev_mid = ListNode(0, head)
        while head and head.next:
            prev_mid = prev_mid.next
            head = head.next.next
        mid = prev_mid.next
        prev_mid.next = None
        return mid

    def merge(left, right):
        dummy = ListNode(0)
        current = dummy
        while left or right:
            if (left and not right) or (left and right and left.val <= right.val):
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        current.next = None
        return dummy.next

    if not head or not head.next:
        return head

    mid = get_mid(head)
    left = sort_list(head)
    right = sort_list(mid)
    return merge(left, right)


assert linked_list_to_python_list(sort_list(python_list_to_linked_list([4, 3, 2, 1]))) == [1, 2, 3, 4]
assert linked_list_to_python_list(sort_list(python_list_to_linked_list([1, 2, 4, 3]))) == [1, 2, 3, 4]
assert linked_list_to_python_list(sort_list(python_list_to_linked_list([4, 2, 1, 3]))) == [1, 2, 3, 4]
assert linked_list_to_python_list(sort_list(python_list_to_linked_list([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]
assert linked_list_to_python_list(sort_list(python_list_to_linked_list([]))) == []
assert linked_list_to_python_list(sort_list(python_list_to_linked_list([4,19,14,5,-3,1,8,5,11,15])))
