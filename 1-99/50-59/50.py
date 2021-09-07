"""
Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:
Input: 2.00000, 10,  Output: 1024.00000

Example 2:
Input: 2.10000, 3,  Output: 9.26100

Example 3:
Input: 2.00000, -2,  Output: 0.25000,  Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
-100.0 < x < 100.0, n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""

"""
Of course this is batteries included with Python. An alternative implementation is provided below. We cannot keep
multiplying in a range over n as n can be huge. Instead we realise that we can use binary decomposition but 
representing powers instead of integers. For example bin(13)=b1101. We go through the binary representation backwards,
representing a power of 13 as powers of 1, 4, 8 multiplied together. The next power in the sequence can be trivially 
calculated from the previous one (e.g. power of 8 = power by 4 * power by 4). We just have to watch out for 
float precision constraints. Floats generally round out at 17dp so we check this after every iteration of the power 
sequence and terminate early if appropriate. We also have to watch out for the negative sign if present.
"""


def my_pow(x, n):
    if n < 0:
        x = 1/x
    sign = -1 if (x < 0 and n % 2) else 1
    res, last_power = 1, 0
    for pow_2, bit in enumerate(reversed(bin(abs(n))[2:])):
        power = abs(x) if not pow_2 else last_power * last_power
        last_power = power
        if bit == '1':
            res *= power
        if 0 < last_power < 10**-17:
            return 0
        elif last_power > 10**17:
            return float('inf') * sign
    return res * sign


assert my_pow(10.0, 0) == 1
assert my_pow(10.0, 5) == 100000
assert my_pow(10.0, -1) == 0.1
assert my_pow(2.00000, 10) == 1024.00000
assert my_pow(2.10000, 3) == 9.261000000000001
assert my_pow(2.00000, -2) == 0.25000
assert my_pow(-2.0, 2) == 4.0
assert my_pow(-13.62608, 3) == -2529.9550389278597
