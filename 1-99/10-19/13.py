"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol  I  V  X   L   C    D    M
    Value   1  5  10  50  100  500  1000

For example, two is written as II in Roman numerals, just two one's added together. Twelve is written as, XII,
which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III",  Output: 3

Example 2:
Input: "IV",  Output: 4

Example 3:
Input: "IX",  Output: 9

Example 4:
Input: "LVIII",  Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV",  Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

"""
This problem is, like the previous one, fairly simple: we iterate through the string, adding to the number as we go. 
The faster version uses a series of if statements, whilst the neat version condenses them using a dictionary.
"""


def roman_to_int_fast(s):
    num = 0
    last_seen = 0
    for char in s:
        if char == 'M':
            num += 800 if last_seen == 100 else 1000
            last_seen = 1000
        elif char == 'D':
            num += 300 if last_seen == 100 else 500
            last_seen = 500
        elif char == 'C':
            num += 80 if last_seen == 10 else 100
            last_seen = 100
        elif char == 'L':
            num += 30 if last_seen == 10 else 50
            last_seen = 50
        elif char == 'X':
            num += 8 if last_seen == 1 else 10
            last_seen = 10
        elif char == 'V':
            num += 3 if last_seen == 1 else 5
            last_seen = 5
        else:
            num += 1
            last_seen = 1
    return num


def roman_to_int_neat(s):
    num = 0
    last_seen = 0
    conversion = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for char in s:
        converted = conversion[char]
        num += converted - 2*last_seen if converted > last_seen else converted
        last_seen = converted
    return num


assert roman_to_int_fast('III') == roman_to_int_neat('III') == 3
assert roman_to_int_fast('IV') == roman_to_int_neat('IV') == 4
assert roman_to_int_fast('IX') == roman_to_int_neat('IX') == 9
assert roman_to_int_fast('LVIII') == roman_to_int_neat('LVIII') == 58
assert roman_to_int_fast('MCMXCIV') == roman_to_int_neat('MCMXCIV') == 1994



