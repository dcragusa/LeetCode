"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
- MinStack() initializes the stack object.
- push(int val) pushes the element val onto the stack.
- pop() removes the element on the top of the stack.
- top() gets the top element of the stack.
- getMin() retrieves the minimum element in the stack.

Example 1:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

"""
We can easily implement push, pop, and top on top of a standard Python list in O(1) time. Slightly more challenging is
keeping track of and returning minimums in O(1) time as well. We can do this by keeping track of the current minimum
and a list of minimum indices (min_indices) in the stack. When we push a new item, if it is equal or less than the 
current minimum, we update the minimum and add the index of the item on the stack to min_indices. When we pop an item
from the stack, if it is equal to the minimum we know we have to pop an item from min_indices and update the minimum.
In this way, getMin is just returning the value of a variable. Because min_indices is also a stack, all operations
run in O(1) time.
"""


class MinStack:

    def __init__(self):
        self.data = []
        self.minimum = float('inf')
        self.min_indices = []

    def push(self, val):
        if val <= self.minimum:
            self.minimum = val
            self.min_indices.append(len(self.data))
        self.data.append(val)

    def pop(self):
        if self.data.pop() == self.minimum:
            self.min_indices.pop()
            self.minimum = self.data[self.min_indices[-1]] if self.min_indices else float('inf')

    def top(self):
        return self.data[-1]

    def getMin(self):
        return self.minimum


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin() == -3
minStack.pop()
assert minStack.top() == 0
assert minStack.getMin() == -2


minStack = MinStack()
minStack.push(2147483646)
minStack.push(2147483646)
minStack.push(2147483647)
assert minStack.top() == 2147483647
minStack.pop()
assert minStack.getMin() == 2147483646
minStack.pop()
assert minStack.getMin() == 2147483646
minStack.pop()
minStack.push(2147483647)
assert minStack.top() == 2147483647
assert minStack.getMin() == 2147483647
minStack.push(-2147483648)
assert minStack.top() == -2147483648
assert minStack.getMin() == -2147483648
minStack.pop()
assert minStack.getMin() == 2147483647
