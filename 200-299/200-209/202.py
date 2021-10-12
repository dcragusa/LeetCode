"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle without 1.
- Those numbers for which this process ends in 1 are happy.

Example 1:
Input: n = 19,  Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false
Explanation:
2^2 = 4
4^2 = 16
1^2 + 6^2 = 37
3^2 + 7^2 = 58
5^2 + 8^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0^2 = 4  <-- cycle without 1
"""

"""
We repeatedly perform the 'happy' determination for each number, then add it to a set, until we find a number we have
seen before. If this number is a 1, the overall number is happy.
"""


def is_happy(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        new_n = 0
        for char in str(n):
            new_n += int(char) ** 2
        n = new_n
    return n == 1


assert is_happy(19) is True
assert is_happy(2) is False
