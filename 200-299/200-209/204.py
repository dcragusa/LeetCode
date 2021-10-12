"""
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10,  Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0,  Output: 0

Example 3:
Input: n = 1,  Output: 0
"""

"""
We implement the sieve of Eratosthenes: we set up a dp array of 1s, of size n. We then iterate from 2 (as numbers below
2 are not primes) to n. If we see that the number is 1 in the primes dp array, we know that this number is a prime. We
then iterate from the next power of the number up to n, in increments of the number, setting those values in the dp
array to 0 (they cannot be prime as they are divisible by the current number). Once we have finished iterating from 2
to n, we simply sum the primes dp array to find the number of primes.
"""


def count_primes(n):
    if n <= 2:
        return 0
    primes = [1] * n
    primes[0] = primes[1] = 0
    for num in range(2, n):
        if primes[num]:
            for prime_mult in range(num*num, n, num):
                primes[prime_mult] = 0
    return sum(primes)


assert count_primes(10) == 4
assert count_primes(0) == 0
assert count_primes(1) == 0
assert count_primes(499979) == 41537

