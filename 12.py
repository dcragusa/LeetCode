"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol  I  V  X   L   C    D    M
    Value   1  5  10  50  100  500  1000

For example, two is written as II in Roman numerals, just two one's added together. Twelve is written as XII,
which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: 3, Output: "III"

Example 2:
Input: 4, Output: "IV"

Example 3:
Input: 9, Output: "IX"

Example 4:
Input: 58, Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: 1994, Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

"""
This problem is fairly simple: we decrease the number, adding on to the output string as we go. The faster version
uses a series of while loops, whilst the neat version condenses them using a dictionary.
"""


def int_to_roman_fast(num):
    output = ''
    while num >= 1000:
        output += 'M'
        num -= 1000
    while num >= 900:
        output += 'CM'
        num -= 900
    while num >= 500:
        output += 'D'
        num -= 500
    while num >= 400:
        output += 'CD'
        num -= 400
    while num >= 100:
        output += 'C'
        num -= 100
    while num >= 90:
        output += 'XC'
        num -= 90
    while num >= 50:
        output += 'L'
        num -= 50
    while num >= 40:
        output += 'XL'
        num -= 40
    while num >= 10:
        output += 'X'
        num -= 10
    while num >= 9:
        output += 'IX'
        num -= 9
    while num >= 5:
        output += 'V'
        num -= 5
    while num >= 4:
        output += 'IV'
        num -= 4
    while num:
        output += 'I' * num
    return output


def int_to_roman_neat(num):
    output = ''
    conversion = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
        50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    for n, roman in conversion.items():
        while num >= n:
            output += roman
            num -= n
    return output


assert int_to_roman_fast(3) == int_to_roman_neat(3) == 'III'
assert int_to_roman_fast(4) == int_to_roman_neat(4) == 'IV'
assert int_to_roman_fast(9) == int_to_roman_neat(9) == 'IX'
assert int_to_roman_fast(58) == int_to_roman_neat(58) == 'LVIII'
assert int_to_roman_fast(1994) == int_to_roman_neat(1994) == 'MCMXCIV'
