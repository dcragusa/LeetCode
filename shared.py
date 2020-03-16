
class ListNode:
    def __init__(self, x):
        self.val, self.next = x, None

    def __repr__(self):
        return f'{self.val}'


def linked_list_to_python_list(head):
    python_list = []
    while head:
        python_list.append(head.val)
        head = head.next
    return python_list
