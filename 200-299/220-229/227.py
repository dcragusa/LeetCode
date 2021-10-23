"""
Given a string s which represents an expression, evaluate this expression and return its value. The integer division
should truncate toward zero. You may assume that the given expression is always valid. Note: You are not allowed to use
any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = '3+2*2',  Output: 7

Example 2:
Input: s = ' 3/2 ',  Output: 1

Example 3:
Input: s = ' 3+5 / 2 ',  Output: 5
"""

"""
This is somewhat similar to 224, except without brackets but having to pay attention to the order of operations. We
make two passes: a first one that tokenises the input string and performs multiplication and division. We then go
through the tokens and complete the calculation by performing additions and subtractions.
"""

from operator import add, sub, mul, floordiv


def calculate(s):

    tokens = []
    operation = None

    idx = 0
    while idx < len(s):
        char = s[idx]
        if char == ' ':
            idx += 1
            continue
        if char == '*':
            operation = mul
        elif char == '/':
            operation = floordiv
        elif char == '+':
            tokens.append(add)
        elif char == '-':
            tokens.append(sub)
        else:
            str_num = char
            while idx < len(s) - 1 and (char := s[idx+1]).isdigit():
                str_num += char
                idx += 1
            num = int(str_num)
            if operation is None:
                tokens.append(num)
            else:
                tokens[-1] = operation(tokens[-1], num)
                operation = None
        idx += 1

    num = tokens[0]
    idx = 1
    while idx < len(tokens):
        num = tokens[idx](num, tokens[idx+1])
        idx += 2

    return num


assert calculate('3+2*2') == 7
assert calculate(' 3/2 ') == 1
assert calculate(' 3+5 / 2 ') == 5
assert calculate('-3+2*2') == 1
assert calculate('-10+20/10') == -8
assert calculate('2*3+4') == 10
