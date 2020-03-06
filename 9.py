"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121, Output: true

Example 2:
Input: -121, Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10, Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
"""

"""
The problem is trivial if we convert the number to a string. It is more complex if no string operations are allowed.
First we establish the length of the number, which we can do using math.ceil(math.log10(num+1)). Then we create a
function which returns a particular digit of a number (in reverse order compared to a list: the 0th digit is the 
rightmost digit, going leftwards). This works by first doing modulo 10**(digit-1), which chops off everything to the
left of the requested digit. Then we divide by 10**digit, which chops off everything to the right. Finally, we 
iterate over half of the number length, comparing digits from opposite ends of the number.
"""

# def is_palindrome(num):
#     return str(num) == str(num)[::-1]

import math


def get_num_digit(num, digit):
    return num % 10**(digit+1) // 10**digit


def is_palindrome(num):
    if num < 0:
        return False
    num_length = math.ceil(math.log10(num+1))
    for i in range((num_length // 2) + 1):
        if get_num_digit(num, i) != get_num_digit(num, num_length-i-1):
            return False
    return True


assert is_palindrome(121) is True
assert is_palindrome(9999) is True
assert is_palindrome(-121) is False
assert is_palindrome(10) is False
