"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:[ 1->4->5, 1->3->4, 2->6 ],  Output: 1->1->2->3->4->4->5->6
"""

"""
First we eliminate any empty linked lists from the list of lists. Then we sort the list of lists in descending order
(pops are O(1) at the end of a list). We add the node from the end of the list to the new linked list, and insert the
next item from the popped list in place by taking advantage of a modification of Python's bisect.insort to work on
reversed lists.
Time complexity: initial sort O(N log N) - only occurs once, pop O(1), insert inplace O(N) therefore O(Nk)
                 where N is the number of nodes in the merged list.
Space complexity: the only thing we are creating is the solution, so O(1).
"""

from operator import attrgetter
from shared import python_list_to_linked_list, linked_list_to_python_list


def reverse_insort(lists, node):
    low, high = 0, len(lists)
    while low < high:
        mid = (low + high) // 2
        if node.val > lists[mid].val:
            high = mid
        else:
            low = mid+1
    lists.insert(low, node)


def merge_k_lists(list_of_lists):
    head = current = None
    list_of_lists = [linked_list for linked_list in list_of_lists if linked_list]
    sorted_lists = sorted(list_of_lists, key=attrgetter('val'), reverse=True)
    while sorted_lists:
        node = sorted_lists.pop()
        if head is None:
            head = current = node
        else:
            current.next = node
            if not sorted_lists:
                return head
            current = current.next
        if node.next:
            reverse_insort(sorted_lists, node.next)
    return head


one = python_list_to_linked_list([1, 4, 5])
two = python_list_to_linked_list([1, 3, 4])
three = python_list_to_linked_list([2, 6])
assert linked_list_to_python_list(merge_k_lists([one, two, three])) == [1, 1, 2, 3, 4, 4, 5, 6]

assert linked_list_to_python_list(merge_k_lists([[]])) == []

one = python_list_to_linked_list([1])
assert linked_list_to_python_list(merge_k_lists([one])) == [1]
