"""
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123", "132", "213", "231", "312", "321"
Given n and k, return the kth permutation sequence.

Note:
Given n will be between 1 and 9 inclusive. Given k will be between 1 and n! inclusive.

Example 1:
Input: n = 3, k = 3,  Output: "213"

Example 2:
Input: n = 4, k = 9,  Output: "2314"
"""

"""
This can be done in a one-liner using itertools.islice and itertools.permutations, but it requires generating 
(however efficiently) the entire sequence of permutations up to k.
A faster version can be implemented by exploiting the applications of factoradic numbers to permutations 
(https://en.wikipedia.org/wiki/Factorial_number_system). All we have to to is calculate the factoradic number of k 
(minus 1, because factoradic numbers are 0-indexed and the kth permutation is 1-indexed). We pad it with 0s to make 
sure we pick every element from the set of n. Then we iterate backwards, popping off the number of that index from the 
set of n until we have exhausted both the factoradic number and set of n. The result is the kth permutation.
"""


from itertools import islice, permutations, count


def get_permutation_slow(n, k):
    return ''.join(map(str, next(islice(permutations(range(1, n+1), n), k-1, None))))


def get_permutation_fast(n, k):
    k -= 1
    factoradics = []
    for i in count(start=1):
        factoradics.append(k % i)
        k //= i
        if not k:
            break
    factoradics = factoradics + [0]*(n - len(factoradics))
    result, nums = [], list(range(1, n+1))
    for factoradic in reversed(factoradics):
        result.append(nums[factoradic])
        nums.pop(factoradic)
    return ''.join(map(str, result))


assert get_permutation_slow(3, 1) == get_permutation_fast(3, 1) == '123'
assert get_permutation_slow(3, 2) == get_permutation_fast(3, 2) == '132'
assert get_permutation_slow(3, 3) == get_permutation_fast(3, 3) == '213'
assert get_permutation_slow(4, 9) == get_permutation_fast(4, 9) == '2314'
assert get_permutation_slow(7, 2982) == get_permutation_fast(7, 2982) == '5172643'
