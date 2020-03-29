
class ListNode:
    def __init__(self, x):
        self.val, self.next = x, None

    def __repr__(self):
        return f'{self.val}'


def python_list_to_linked_list(items):
    head, prev = None, None
    for item in items:
        node = ListNode(item)
        if not head:
            head = node
        if prev:
            prev.next = node
        prev = node
    return head


def linked_list_to_python_list(head):
    python_list = []
    while head:
        python_list.append(head.val)
        head = head.next
    return python_list
