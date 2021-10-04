"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses. If multiple answers are possible,
return any of them. It is guaranteed that the length of the answer string is less than 10^4 for all the given inputs.

Example 1:
Input: numerator = 1, denominator = 2,  Output: '0.5'

Example 2:
Input: numerator = 2, denominator = 1,  Output: '2'

Example 3:
Input: numerator = 2, denominator = 3,  Output: '0.(6)'

Example 4:
Input: numerator = 4, denominator = 333,  Output: '0.(012)'

Example 5:
Input: numerator = 1, denominator = 5,  Output: '0.2'
"""

"""
An annoying problem to solve, mainly due to the number of edge cases. We can implement this using repeated long
division with divmod: when the remainder starts repeating, we know we have found the recurring part.
We exit early if the numerator is 0, as the result will always be 0. We then establish whether the result will be
negative (numerator xor denominator < 0) and proceed by using divmod with absolute values (as it behaves weirdly with
negatives). We establish the integer part of the solution, then proceed to find the decimal part. We repeatedly perform
long division, keeping track of how many tens we have to multiply at each step. We then save the previous remainder,
the number of tens, and the quotient obtained to a dictionary (taking advantage of the fact it is ordered in later 
Python versions). When we find a repetition of both the previous remainder and the number of tens, we stop dividing as
we have entered a cycle and thus found the repeating part of the decimal.
Then we just have to iterate over the division results, appending digits and brackets to the result str as necessary.
"""


def fraction_to_decimal(numerator, denominator):

    if not numerator:
        return '0'

    result = '-' if (numerator < 0) != (denominator < 0) else ''
    numerator, denominator = abs(numerator), abs(denominator)
    quotient, remainder = divmod(numerator, denominator)
    result += str(quotient)
    if not remainder:
        return result

    result += '.'

    divisions = {}
    repeating = None
    while remainder:
        tens = -1
        while remainder < denominator:
            remainder *= 10
            tens += 1
        quotient, new_remainder = divmod(remainder, denominator)
        if (remainder, tens) in divisions:
            repeating = (remainder, tens)
            break
        divisions[remainder, tens] = quotient
        remainder = new_remainder

    for (remainder, tens), quotient in divisions.items():
        if (remainder, tens) == repeating:
            result += '('
        result += ('0' * tens) + str(quotient)
    if repeating:
        result += ')'

    return result


assert fraction_to_decimal(1, 2) == '0.5'
assert fraction_to_decimal(2, 1) == '2'
assert fraction_to_decimal(2, 3) == '0.(6)'
assert fraction_to_decimal(4, 333) == '0.(012)'
assert fraction_to_decimal(1, 5) == '0.2'
assert fraction_to_decimal(1, 7) == '0.(142857)'
assert fraction_to_decimal(10, 7) == '1.(428571)'
assert fraction_to_decimal(1, 90) == '0.01(1)'
assert fraction_to_decimal(1, 99) == '0.(01)'
assert fraction_to_decimal(-50, 8) == '-6.25'
assert fraction_to_decimal(0, -5) == '0'
assert fraction_to_decimal(1, 29) == '0.(0344827586206896551724137931)'
assert fraction_to_decimal(1, 119) == '0.(008403361344537815126050420168067226890756302521)'
