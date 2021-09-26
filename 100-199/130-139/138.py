"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to
any node in the list, or None. Construct a deep copy of the list. The deep copy should consist of exactly n brand
new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and
random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original
list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the o
riginal list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding
two nodes x and y in the copied list, x.random --> y.

Your code will only be given the head of the original linked list. Return the head of the copied linked list.
"""

"""
The logic is similar to 133: we first go through the original linked list, building up a map of old to new (copied)
nodes. Then we go though the map, assigning next and random nodes to match the old nodes.
"""


class Node:
    def __init__(self, x, next_node=None, random_node=None):
        self.val = int(x)
        self.next = next_node
        self.random = random_node


def clone_random_list(head):
    node_map = {}
    while head:
        node_map[head] = Node(head.val)
        head = head.next

    for old_node, new_node in node_map.items():
        new_node.next = node_map[old_node.next]
        new_node.random = node_map[old_node.random]

    return node_map[head]
