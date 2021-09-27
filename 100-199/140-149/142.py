"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return None. There is
a cycle in a linked list if there is some node in the list that can be reached again by continuously following the
next pointer. Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1,  Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0,  Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1,  Output: no cycle
Explanation: There is no cycle in the linked list.
"""

"""
Similar to 141, we just keep a set of seen nodes and return the next pointer if the next pointer is in this set.
"""


def has_cycle(head):
    seen = set()
    while head:
        seen.add(head)
        if head.next in seen:
            return head.next
        head = head.next
    return None
