"""
Given n, how many structurally unique BST's (binary search trees) can store values 1 ... n?

Example:
Input: 3,  Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

"""
This problem is equivalent to finding the Catalan numbers: https://en.wikipedia.org/wiki/Catalan_number. Once this has
been recognised we can implement that formula directly.
"""


from math import factorial


def num_trees(n):
    return factorial(2*n) // (factorial(n+1) * factorial(n))


assert num_trees(3) == 5
