"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor. The integer division should truncate toward zero, which means
losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:
Input: dividend = 10, divisor = 3,  Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3,  Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Note:
Both dividend and divisor will be 32-bit signed integers. The divisor will never be 0.
Assume we are dealing with an environment which can only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 2^31 − 1 when the division
result overflows.
"""

"""
The brute force solution is just to implement repeated subtraction.
We can optimise this by implementing long multiplication/division.
"""

MIN_INT = -2**31
MAX_INT = 2**31 - 1


# def divide(dividend, divisor):
#     sign = 1 if (abs_dividend := abs(dividend)) + (abs_divisor := abs(divisor)) == abs(dividend + divisor) else -1
#     quotient = 0
#     while abs_dividend - abs_divisor >= 0:
#         quotient += 1
#         abs_dividend -= abs_divisor
#     result = quotient * sign
#     if result < MIN_INT:
#         return MIN_INT
#     elif result > MAX_INT:
#         return MAX_INT
#     else:
#         return result


def divide_positive_simple(dividend, divisor):
    quotient = 0
    while dividend >= divisor:
        quotient += 1
        dividend -= divisor
    return quotient, dividend


def multiply_positive_simple(multiplicand, multiplier):
    result = 0
    for _ in range(multiplier):
        result += multiplicand
    return result


def multiply_positive_long(multiplicand, multiplier):
    if multiplicand == 0 or multiplier == 0:
        return 0
    result = 0
    for pow_10, digit in enumerate(reversed(str(multiplier))):
        result += int(str(multiply_positive_simple(multiplicand, int(digit))) + '0'*pow_10)
    return result


def divide(dividend, divisor):
    sign = 1 if (abs_dividend := abs(dividend)) + (abs_divisor := abs(divisor)) == abs(dividend + divisor) else -1
    if abs_divisor > abs_dividend:
        return 0
    dividend = str(abs_dividend)
    working_dividend = ''
    working_quotient = ''
    for digit in dividend:
        working_dividend = int(working_dividend + digit)
        quotient, remainder = divide_positive_simple(working_dividend, abs_divisor)
        working_quotient += str(quotient)
        working_dividend = str(working_dividend - multiply_positive_long(quotient, abs_divisor))

    result = int(working_quotient) * sign
    if result < MIN_INT:
        return MIN_INT
    elif result > MAX_INT:
        return MAX_INT
    else:
        return result


assert divide(2, 3) == 0
assert divide(3, 3) == 1
assert divide(10, 3) == 3
assert divide(7, -3) == -2
assert divide(-7, -3) == 2
assert divide(-7, 3) == -2
assert divide(-2**31, -1) == 2**31 - 1
assert divide(1004958205, -2137325331) == 0
assert divide(-1021989372, -82778243) == 12
