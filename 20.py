"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets are closed by the same type of brackets.
    Open brackets are closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
Input: "()", Output: true

Example 2:
Input: "()[]{}", Output: true

Example 3:
Input: "(]", Output: false

Example 4:
Input: "([)]", Output: false

Example 5:
Input: "{[]}", Output: true
"""


def is_valid(s):
    open_brackets = []
    open_to_closed = {'(': ')', '[': ']', '{': '}'}
    for bracket in s:
        if bracket in open_to_closed:
            open_brackets.append(bracket)
        elif open_brackets and bracket == open_to_closed[open_brackets[-1]]:
            open_brackets.pop()
        else:
            return False
    return not open_brackets


assert is_valid('()') is True
assert is_valid('()[]{}') is True
assert is_valid('(]') is False
assert is_valid('([)]') is False
assert is_valid('{[]}') is True
