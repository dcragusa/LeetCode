"""
Given two strings s and t, return the number of distinct subsequences of s which equals t. A string's subsequence
is a new string formed from the original string by deleting some (can be none) of the characters without disturbing
the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:
Input: s = "rabbbit", t = "rabbit",  Output: 3
Explanation: rabb*it, rab*bit, ra*bbit

Example 2:
Input: s = "babgbag", t = "bag",  Output: 5
Explanation: ba*g***, ba****g, b****ag, **b**ag, ****bag
"""

"""
We can solve this in two ways: recursive and iterative. 
For the recursive way, we recursively iterate across s. If the letters of s and t match, we also recur for the next 
character of t. We can save time by passing indices instead of splitting strings, and we can save additional time by 
memoising the results for each index pair.
For the iterative way, we can utilise dynamic programming. We set up a list of length s, filled with 0s. We then count
backwards across s, putting a 1 in every space that contains the last letter of t. We then count backwards across s
again, counting how many combinations are valid for the penultimate letter of t, and so forth until we have processed
every letter in t. The list now shows the number of valid positions for the whole word, so we return the sum of the 
list. We can perform some optimisations by starting with the list initialised to the last letter of t instead of 0s, 
additionally realising that since we are counting previous letter occurrences, we can skip iterating across the part 
of the result list ending in 0s as these will never affect the answer. Below are the result lists for each step of 
the babgbag/bag and rabbbit/rabbit examples. Note how the final list corresponds to the number of occurrences of the
first letter of t in each position of the 'Explanation' line of the problem statement above.

      babgbag
  g  [0001001]
  a  [0200010]  (the rightmost a has only 1 g after it, but the next a can have 2 g's)
  b  [3010100]  (the two rightmost b's have only 1 a after it, but the leftmost can have 3 a's)
  
      rabbbit
  t  [0000001]
  i  [0000010]
  b  [0011100]
  b  [0021000]
  a  [0300000]
  r  [3000000]
"""

# from functools import lru_cache
#
#
# def num_distinct(s, t):
#
#     len_s, len_t = len(s), len(t)
#     max_t_idx = len_t - 1
#
#     @lru_cache()
#     def helper(s_idx, t_idx):
#         if s_idx == len_s or t_idx == len_t:
#             # out of bounds
#             return 0
#         count = 0
#         if s[s_idx] == t[t_idx]:
#             if t_idx == max_t_idx:
#                 count += 1
#             else:
#                 count += helper(s_idx + 1, t_idx + 1)
#         count += helper(s_idx + 1, t_idx)
#         return count
#
#     return helper(0, 0)


def num_distinct(s, t):

    dp = [(0 if s[i] != t[-1] else 1) for i in range(len(s))]

    for idx_t in reversed(range(len(t)-1)):
        # while dp[-1] == 0:
        #     # stop iterating over this part of the array - it will never affect results
        #     dp.pop()
        prev_letter_sum = 0
        for idx_s in reversed(range(len(dp))):
            dp[idx_s], prev_letter_sum = prev_letter_sum if s[idx_s] == t[idx_t] else 0, prev_letter_sum + dp[idx_s]

    return sum(dp)


assert num_distinct('aab', 'ab') == 2
assert num_distinct('rabbbit', 'rabbit') == 3
assert num_distinct('babgbag', 'bag') == 5
assert num_distinct(
    "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbb"
    "aeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe",
    "bddabdcae"
) == 10582116
assert num_distinct(
    "daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbae"
    "ccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac",
    "ceadbaa"
) == 8556153
assert num_distinct(
    "adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeae"
    "eabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc",
    "bcddceeeebecbc"
) == 700531452
