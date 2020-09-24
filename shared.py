
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


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

    def __repr__(self):
        return repr(self.val)

    def pprint(self, level=0):
        # rotate the output 90* clockwise :)
        if self.right:
            self.right.pprint(level+1)
        print('%s%s' % ('\t'*level, self.val))
        if self.left:
            self.left.pprint(level+1)

    def __eq__(self, other):
        return (self.val, self.left, self.right) == (other.val, other.left, other.right)
