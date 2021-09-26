"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (list[Node]) of its neighbours.

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with
val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set
of neighbours of a node in the graph. The given node will always be the first node with val = 1. You must return the
copy of the given node as a reference to the cloned graph.
"""

"""
We first go through the original graph, creating a map from old to new (copied) nodes by depth-first-search. Then we
go through the resulting map, assigning new node neighbours to match old node neighbours.
"""


class Node:
    def __init__(self, val, neighbours=None):
        self.val = val
        self.neighbours = neighbours if neighbours is not None else []


def clone_graph(node):
    if node is None:
        return None

    node_map = {}

    def map_nodes(node):
        if node in node_map:
            return
        node_map[node] = Node(node.val)
        for neighbour in node.neighbours:
            map_nodes(neighbour)

    map_nodes(node)

    for old_node, new_node in node_map.items():
        for neighbour in old_node.neighbours:
            new_node.neighbours.append(node_map[neighbour])

    return node_map[node]
