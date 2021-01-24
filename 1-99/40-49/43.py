"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3", Output: "6"

Example 2:
Input: num1 = "123", num2 = "456", Output: "56088"

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

"""
Fairly trivial to convert strings to numbers indirectly using ord(), also helpful is Python's infinite integers.
"""


def str_to_num(s):
    num = 0
    for pow_10, digit in enumerate(reversed(s)):
        num += (ord(digit) - ord('0')) * 10**pow_10
    return num


def multiply(num1, num2):
    return str(str_to_num(num1) * str_to_num(num2))


assert multiply('2', '3') == '6'
assert multiply('123', '456') == '56088'
