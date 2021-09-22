"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day. On each day, you
may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you
can sell it then immediately buy it on the same day. Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7, 1, 5, 3, 6, 4],  Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3. Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1, 2, 3, 4, 5],  Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4.

Example 3:
Input: prices = [7, 6, 4, 3, 1],  Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
"""

"""
Seeing as we can sell/buy stock on the same day, this is simply equivalent to finding the total increases from the
previous number over the array (functionally for example 2, there is no difference between buying on day 1 and selling
on day 5, and buying on day 1, selling then buying on day 2, selling then buying on day 3 etc.).
"""


def max_profit(prices):
    profit = 0
    last_price = prices[0]
    for price in prices[1:]:
        if price > last_price:
            profit += price - last_price
        last_price = price
    return profit


assert max_profit([7, 1, 5, 3, 6, 4]) == 7
assert max_profit([1, 2, 3, 4, 5]) == 4
assert max_profit([7, 6, 4, 3, 1]) == 0
