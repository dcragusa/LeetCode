"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word: Insert a character, Delete a character, Replace a character.

Example 1:
Input: word1 = "horse", word2 = "ros",  Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r'),
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution",  Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

"""
This is the Levenshtein distance: https://en.wikipedia.org/wiki/Levenshtein_distance.
We can implement a recursive or iterative approach (https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm).

For the recursive approach, we count along the strings, comparing each character. If the characters are the same, we
skip them, otherwise we take the minimum of 3 options: insert the second character; delete the first character; 
swap the characters. This is a pretty slow and inefficient approach for longer strings.

For the iterative approach, we create a (s1+1 by s2+1) matrix showing the cost of getting from s1 to s2. The first row
and column are set to the indices of s2 and s1 respectively (it would take 3 steps to get to the 3rd letter of s2 if
s1 is an empty string, and vice versa). Then we go through the matrix left to right downwards, setting each value - 
which is the minimum of: the value above (i-1) + 1, representing deleting a character; the value to the left (j-1) + 1,
representing adding a character; and the value to the top left (i-1, j-1), representing swapping the characters. 1 is
added to this if the characters are different and 0 if they are equal. The solution is the value at the bottom right,
which is the total cost of getting from s1 to s2.
"""


from functools import lru_cache


@lru_cache()
def min_distance_recursive(word1, word2):
    if not word1:
        return len(word2)
    elif not word2:
        return len(word1)
    a, rest_a, b, rest_b = word1[0], word1[1:], word2[0], word2[1:]
    if a == b:
        return min_distance_recursive(rest_a, rest_b)
    else:
        return 1 + min(
            min_distance_recursive(b+word1, word2),
            min_distance_recursive(rest_a, word2),
            min_distance_recursive(b+rest_a, word2)
        )


def min_distance_iterative(word1, word2):

    len1, len2 = len(word1) + 1, len(word2) + 1
    distances = [[0 for _ in range(len2)] for _ in range(len1)]

    for i in range(1, len1):
        distances[i][0] = i
    for j in range(1, len2):
        distances[0][j] = j

    for i in range(1, len1):
        for j in range(1, len2):
            distances[i][j] = min(
                distances[i-1][j] + 1,
                distances[i][j-1] + 1,
                distances[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1)
            )

    return distances[len1-1][len2-1]


assert min_distance_recursive('horse', 'ros') == min_distance_iterative('horse', 'ros') == 3
assert min_distance_recursive('intention', 'execution') == min_distance_iterative('intention', 'execution') == 5
# assert min_distance_recursive('pneumonoultramicroscopicsilicovolcanoconiosis', 'stereomicroscopically') == 30
assert min_distance_iterative('pneumonoultramicroscopicsilicovolcanoconiosis', 'stereomicroscopically') == 30
