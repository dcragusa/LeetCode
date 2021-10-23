"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result
of the evaluation. Note: You are not allowed to use any built-in function which evaluates strings as expressions.

Example 1:
Input: s = '1 + 1',  Output: 2

Example 2:
Input: s = ' 2-1 + 2 ',  Output: 3

Example 3:
Input: s = '(1+(4+5+2)-3)+(6+8)',  Output: 23
"""

"""
We implement a stack to deal with brackets. Each state in the stack has a number, negative flag, and operation
function. We use __slots__ to save on memory. The stack is initialised with an empty state. We iterate over indices
of s: every time a bracket is encountered we add a new empty state to the stack. All operations are performed on the
last state in the stack so we keep calculations inside the bracket contained. When we find a closing bracket, we take
the number in the last state, pop the state (as we are done with that set of brackets) and apply that number to the
new last state in the stack. We take care to distinguish between the minus sign as an operator or a negative modifier.
We also have a sub-loop to take care of successive numbers together to make a larger one, e.g. 123. At the end of s,
we will only have one state left on the stack (the initial one) so we return the number from this.
"""

from operator import add, sub


class CalcState:
    __slots__ = ['num', 'negative', 'operation']

    def __init__(self):
        self.num, self.negative, self.operation = None, False, None


def calculate(s):
    state_stack = [CalcState()]

    def process_num(num):
        state = state_stack[-1]
        if state.num is None:
            state.num = num * (-1 if state.negative else 1)
            state.negative = False
        else:
            state.num = state.operation(state.num, num)
            state.operation = None

    idx = 0
    while idx < len(s):
        if (char := s[idx]) == ' ':
            idx += 1
            continue
        state = state_stack[-1]
        if char == '(':
            state_stack.append(CalcState())
        elif char == ')':
            num = state.num
            state_stack.pop()
            process_num(num)
        elif char == '-':
            if state.num is None:
                state.negative = True
            else:
                state.operation = sub
        elif char == '+':
            state.operation = add
        else:
            str_num = char
            while idx < len(s) - 1 and (char := s[idx+1]).isdigit():
                str_num += char
                idx += 1
            process_num(int(str_num))
        idx += 1

    return state_stack[-1].num


assert calculate('1 + 1') == 2
assert calculate(' 2-1 + 2 ') == 3
assert calculate('-1 + 2') == 1
assert calculate('-25-(1+4)') == -30
assert calculate('(1+(4+5+2)-3)+(6+8)') == 23
assert calculate('- (3 + (4 + 5))') == -12
assert calculate('1-11') == -10
assert calculate('-25-15+50') == 10
assert calculate('-(3+4)+5') == -2
