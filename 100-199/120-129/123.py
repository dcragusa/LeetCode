"""
You are given an array prices where prices[i] is the price of a given stock on the ith day. Find the maximum profit
you can achieve. You may complete at most two transactions. Note: You may not engage in multiple transactions
simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3, 3, 5, 0, 0, 3, 1, 4],  Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1, 2, 3, 4, 5],  Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.

Example 3:
Input: prices = [7, 6, 4, 3, 1],  Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Example 4:
Input: prices = [1],  Output: 0
"""

"""
One naive solution might be to reuse the solution from 121: we know that the array must be split in two to get two
profits from a single transaction each (as they cannot overlap). We simply iterate through the length of the array,
splitting it in each possible place and calculating the resulting profit from two transactions. However, this is
horrendously inefficient.
A much better method is to iterate from left to right across the array, finding the maximum profit obtainable at each
position from a single transaction thus far. Then, iterate backwards across the array, splitting the profit into the 
left side profit previously obtained, and the profit obtainable from a transaction made on the right hand side. The
max profit can thus be obtained by finding the maximum sum of these left and right hand side profits across the array.
"""

# def max_profit_single(prices):
#     most_profit = 0
#     if not prices:
#         return most_profit
#     min_price = prices[0]
#     for price in prices[1:]:
#         most_profit = max(most_profit, price - min_price)
#         min_price = min(min_price, price)
#     return most_profit
#
#
# def max_profit(prices):
#     most_profit = 0
#     for i in range(len(prices)):
#         most_profit = max(most_profit, max_profit_single(prices[:i]) + max_profit_single(prices[i:]))
#     return most_profit


def max_profit(prices):
    len_prices = len(prices)
    profits = [0] * len_prices

    min_price = prices[0]
    for i in range(1, len_prices):
        min_price = min(min_price, prices[i])
        profits[i] = max(profits[i-1], prices[i] - min_price)

    most_profit = profits[-1]

    max_price = 0
    for i in reversed(range(1, len_prices)):
        max_price = max(max_price, prices[i])
        right_profit = max_price - prices[i]
        left_profit = profits[i-1]
        most_profit = max(most_profit, left_profit + right_profit)

    return most_profit


assert max_profit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
assert max_profit([1, 2, 3, 4, 5]) == 4
assert max_profit([7, 6, 4, 3, 1]) == 0
assert max_profit([1]) == 0
assert max_profit([7, 1, 5, 3, 4, 6, 4, 5]) == 7
assert max_profit([6, 1, 3, 2, 4, 7]) == 7
assert max_profit([14, 9, 10, 12, 4, 8, 1, 16]) == 19
assert max_profit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 13
assert max_profit([1, 2, 4, 2, 5, 7]) == 8
assert max_profit([2, 1, 11, 4, 7]) == 13
assert max_profit([3, 2, 6, 5, 0, 3]) == 7
