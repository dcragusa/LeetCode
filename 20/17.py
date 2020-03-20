"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations (those on telephone
buttons) that the number could represent.

2: ABC, 3: DEF, 4: GHI, 5: JKL, 6: MNO, 7: PQRS, 8: TUV, 9: WXYZ

Example:
Input: "23", Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

"""
The solution is fairly trivial with itertools.product.
"""


import itertools

phone_nums = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}


def letter_combinations(digits):
    if not digits:
        return []
    return [''.join(product) for product in itertools.product(*[phone_nums[digit] for digit in digits])]


assert letter_combinations('') == []
assert letter_combinations('2') == ['a', 'b', 'c']
assert letter_combinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
