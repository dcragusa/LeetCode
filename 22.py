"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
['((()))', '(()())', '(())()', '()(())', '()()()']
"""

"""
We start with one pair of parentheses, which can only be (). For each additional pair, we add an open bracket to the 
front [(()], then iterate across the solutions inserting a close bracket after every available open bracket [()(),(())].
Via recursion we can apply this method to any number of parentheses.
"""


def generate_parentheses(n):
    if n == 0:
        return set()
    if n == 1:
        return {'()'}
    else:
        solutions = set()
        for solution in generate_parentheses(n-1):
            for idx, char in enumerate(solution := '(' + solution):
                if char == '(':
                    solutions.add(solution[:idx+1]+')'+solution[idx+1:])
        return solutions


assert generate_parentheses(0) == set()
assert generate_parentheses(1) == {'()'}
assert generate_parentheses(2) == {'()()', '(())'}
assert generate_parentheses(3) == {'((()))', '(()())', '(())()', '()(())', '()()()'}
assert generate_parentheses(4) == {
    '(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()',
    '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()'
}
assert generate_parentheses(5) == {
    '((((()))))', '(((()())))', '(((())()))', '(((()))())', '(((())))()', '((()(())))', '((()()()))', '((()())())',
    '((()()))()', '((())(()))', '((())()())', '((())())()', '((()))(())', '((()))()()', '(()((())))', '(()(()()))',
    '(()(())())', '(()(()))()', '(()()(()))', '(()()()())', '(()()())()', '(()())(())', '(()())()()', '(())((()))',
    '(())(()())', '(())(())()', '(())()(())', '(())()()()', '()(((())))', '()((()()))', '()((())())', '()((()))()',
    '()(()(()))', '()(()()())', '()(()())()', '()(())(())', '()(())()()', '()()((()))', '()()(()())', '()()(())()',
    '()()()(())', '()()()()()'
}
