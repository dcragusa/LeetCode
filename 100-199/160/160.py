"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return None.

For example, the following two linked lists begin to intersect at node c1:

  a1 - a2
        \
        c1 - c2 - c3
        /
  b1 - b2

The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.
"""

"""
For a solution where we don't care about memory, we can simply maintain a set of seen values that we add to iterating 
over headA, then check to see if there are any seen nodes in headB. If we find one, that is the intersection node.
For an O(1) memory solution, we first have to establish the length of the two linked lists. We then iterate through
the longer list until both lists have equal nodes remaining. At that point we iterate through both lists simultaneously
to see if there is an intersection (by necessity, if there is an intersection the two lists will have equal length).
"""


# def get_intersection_node(headA, headB):
#     seen = set()
#     while headA:
#         seen.add(headA)
#         headA = headA.next
#     while headB:
#         if headB in seen:
#             return headB
#         headB = headB.next


def get_intersection_node(headA, headB):

    def get_length(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return head

    len_a, len_b = get_length(headA), get_length(headB)

    if len_a > len_b:
        for _ in range(len_a - len_b):
            headA = headA.next
    if len_b > len_a:
        for _ in range(len_b - len_a):
            headB = headB.next

    while headA and headB:
        if headA is headB:
            return headA
        headA = headA.next
        headB = headB.next
