"""
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without
any intervening characters.

Example 1:
Input: s = 'barfoothefoobarman',  words = ['foo', 'bar'],  Output: [0, 9]
Explanation: Substrings starting at index 0 and 9 are 'barfoo' and 'foobar' respectively.
The output order does not matter, returning [9, 0] is fine too.

Example 2:
Input: s = 'wordgoodgoodgoodbestword',  words = ['word', 'good', 'best', 'word'],  Output: []
"""

"""
The naive solution constructs a set of possible concatenations then iterates across the string checking to see if a
slice of the appropriate length is in that set. However, this rapidly exhausts memory due to the factorial quality of
the set of concatenations, and so is suitable only for a short list of words.

Another solution goes through s and examines for one word at a time. If found, it examines more of the string to check 
if the rest of it is a valid concatenation, by using a Counter(). Slightly optimised by only copying the counter if a 
valid match has been found and the rest of the string is being examined.

The above suffers from checking the same characters multiple times (as the window moves, and the rest of a potential
match is being checked). This can be optimised by only starting in as many places as the word length, and iterating
through the remainder of the string putting words in a stack and counter. There is a match if the substring counter is 
equal to the words counter. This approach only checks each possible word length substring in the input string once.
"""

# from itertools import permutations
#
#
# def find_substrings(s, words):
#     if not s or not words:
#         return []
#     len_substring = sum([len(word) for word in words])
#     substrings = {''.join(combination) for combination in permutations(words, len(words))}
#     indices = []
#     if len_substring <= len(s):
#         for i in range(len(s)-len_substring+1):
#             if s[i:i+len_substring] in substrings:
#                 indices.append(i)
#     return indices


# from collections import Counter
#
#
# def find_substrings(s, words):
#     if not s or not words:
#         return []
#     len_substring = (word_length := len(words[0])) * len(words)
#     if len_substring > len(s):
#         return []
#     words_counter = Counter(words)
#     indices = []
#     for idx in range(len(s) - len_substring + 1):
#         words_counter_copy, words_counter_copied = words_counter, False
#         for substring_idx in range(idx, idx+len_substring, word_length):
#             if (temp_substring := s[substring_idx:substring_idx+word_length]) in words_counter_copy:
#                 if not words_counter_copied:
#                     words_counter_copy, words_counter_copied = words_counter.copy(), True
#                 if words_counter_copy[temp_substring] == 1:
#                     del words_counter_copy[temp_substring]
#                 else:
#                     words_counter_copy[temp_substring] -= 1
#             else:
#                 break
#         if not words_counter_copy:
#             indices.append(idx)
#     return indices


from collections import Counter, deque


def find_substrings(s, words):
    if not s or not words:
        return []
    len_substring = (word_length := len(words[0])) * len(words)
    if len_substring > len(s):
        return []
    words_counter = Counter(words)
    indices = []
    for start_idx in range(word_length):
        idx = 0
        word_stack = deque()
        substring_counter = Counter()
        while start_idx + idx * word_length < len(s):
            word_stack.append(substring := s[start_idx+idx*word_length:start_idx+(idx+1)*word_length])
            substring_counter[substring] += 1
            if len(word_stack) == len(words):
                if substring_counter == words_counter:
                    indices.append(start_idx+(idx+1)*word_length - len_substring)
                removing = word_stack.popleft()
                if substring_counter[removing] == 1:
                    del substring_counter[removing]
                else:
                    substring_counter[removing] -= 1
            idx += 1
    return indices


assert find_substrings('', []) == []
assert find_substrings('barfoothefoobarman', ['foo', 'bar']) == [0, 9]
assert find_substrings('abababab', ['a', 'b', 'a']) == [0, 2, 4]
assert find_substrings('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']) == []
assert find_substrings('lingmindraboofooowingdingbarrwingmonkeypoundcake',
                       ['fooo', 'barr', 'wing', 'ding', 'wing']) == [13]
assert find_substrings(
    'pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcf'
    'nrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhm'
    'pchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhntt'
    'gmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpip'
    'guhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhug'
    'bikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxc'
    'obxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufj'
    'hzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevs'
    'vpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjn'
    'rpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaev'
    'rbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrn'
    'txqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhov'
    'weaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbb'
    'xncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichm'
    'fidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel',
    [
        'dhvf', 'sind', 'ffsl', 'yekr', 'zwzq', 'kpeo', 'cila', 'tfty', 'modg',
        'ztjg', 'ybty', 'heqg', 'cpwo', 'gdcj', 'lnle', 'sefg', 'vimw', 'bxcb'
    ]) == [935]


# from collections import deque, defaultdict, Counter
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         if not words:
#             return []
#         s_len, word_len, word_total = len(s), len(words[0]), len(words) * len(words[0])
#         count, footprint, res = Counter(words), defaultdict(deque), []
#
#         for start in range(word_len):
#             footprint.clear()
#             end = start
#             while start + word_total <= s_len:
#                 sub = s[end:end + word_len]
#                 end += word_len
#                 if sub in count:
#                     queue = footprint[sub]
#                     queue.append(end)
#                     while queue[0] < start:
#                         queue.popleft()
#                     if len(queue) > count[sub]:
#                         start = queue.popleft()
#                     if start + word_total == end:
#                         res.append(start)
#                 else:
#                     start = end
#         return res
