"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, and /. Each
operand may be an integer or another expression. Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid. That means the expression always evaluates to a result,
and there will not be any division by zero operation.

Example 1:
Input: tokens = ['2', '1', '+', '3', '*'],  Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ['4', '13', '5', '/', '+'],  Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'],  Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

"""
In RPN, operators come after the numbers. So all we have to do is add numbers to a stack, and when we find an operator,
pop two items off the stack and put the result of the operation back on. We implement a custom division function so 
we can truncate towards 0 based on whether the result is positive or negative.
"""

from operator import add, sub, mul
from math import floor, ceil


def towards_zero_div(a, b):
    total = a / b
    truncate = floor if total > 0 else ceil
    return truncate(total)


operators = {'+': add, '-': sub, '*': mul, '/': towards_zero_div}


def evaluate_rpn(tokens):
    stack = []
    for item in tokens:
        if item in operators:
            num2, num1 = stack.pop(), stack.pop()
            num = operators[item](num1, num2)
        else:
            num = int(item)
        stack.append(num)
    return int(stack[0])


assert evaluate_rpn(['2', '1', '+', '3', '*']) == 9
assert evaluate_rpn(['4', '13', '5', '/', '+']) == 6
assert evaluate_rpn(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']) == 22
assert evaluate_rpn(['18']) == 18
assert evaluate_rpn(['0', '3', '/']) == 0
assert evaluate_rpn(['3', '11', '+', '5', '-']) == 9



