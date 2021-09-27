"""
Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked
list if there is some node in the list that can be reached again by continuously following the next pointer.

Example 1:
Input: head = [3,2,0,-4], pos = 1,  Output: True
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0,  Output: True
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1,  Output: False
Explanation: There is no cycle in the linked list.
"""

"""
Fairly simple, we just keep a set of seen nodes and return True if the next pointer is in this set.
"""


def has_cycle(head):
    seen = set()
    while head:
        seen.add(head)
        if head.next in seen:
            return True
        head = head.next
    return False
