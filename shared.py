from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val, self.next = x, None

    def __repr__(self):
        return f'{self.val}'


def python_list_to_linked_list(items: list) -> ListNode:
    head, prev = None, None
    for item in items:
        node = ListNode(item)
        if not head:
            head = node
        if prev:
            prev.next = node
        prev = node
    return head


def linked_list_to_python_list(head: ListNode) -> list:
    python_list = []
    while head:
        python_list.append(head.val)
        head = head.next
    return python_list


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

    def __repr__(self):
        return repr(self.val)

    def pprint(self, level=0):
        # rotate the output 90* clockwise :)
        if self.right:
            self.right.pprint(level + 1)
        print('%s%s' % ('\t' * level, self.val))
        if self.left:
            self.left.pprint(level + 1)

    def __eq__(self, other):
        return (self.val, self.left, self.right) == (other.val, other.left, other.right)


def list_to_tree(items: list) -> Optional[TreeNode]:
    if not items:
        return None

    root = TreeNode(items[0])
    idx = 1
    nodes = deque([root])

    while True:
        if idx >= len(items):
            return root
        node = nodes.popleft()
        if idx < len(items) and (item := items[idx]) is not None:
            node.left = TreeNode(item)
            nodes.append(node.left)
        idx += 1
        if idx < len(items) and (item := items[idx]) is not None:
            node.right = TreeNode(item)
            nodes.append(node.right)
        idx += 1


class Node:
    def __init__(self, val, neighbours=None):
        self.val = val
        self.neighbours = neighbours if neighbours is not None else []
