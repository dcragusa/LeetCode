"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
Find the maximum profit you can achieve. You may complete at most k transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2, 4, 1],  Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3, 2, 6, 5, 0, 3],  Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

"""
Firstly, we special-case the situation in which there are more transactions than half the length of the prices array:
this means that all possible transactions can take place, so we calculate the maximum profit in one pass as per problem
122. Otherwise, we set up a dp array with k rows (plus an initial dummy row) and columns of the same length as prices.
We go through the array, starting from the second row to avoid the dummy row. For our first row, we calculate the max
profit achievable from a single transaction. The second row calculates the profit achievable from two transactions, by
finding the best place to split the previous row into two. Once we have iterated through the entire dp array, the 
profit will be the last value.
"""


def max_profit(prices, k):
    len_prices = len(prices)

    if k > len_prices // 2:
        profit = 0
        for i in range(1, len_prices):
            profit += max(prices[i] - prices[i-1], 0)
        return profit

    dp = [[0] * len_prices for _ in range(k + 1)]
    for i in range(1, k+1):
        profit = -prices[0]
        for j in range(1, len_prices):
            dp[i][j] = max(dp[i][j-1], profit + prices[j])
            profit = max(profit, -prices[j] + dp[i-1][j])

    return dp[-1][-1]


assert max_profit([2, 4, 1], 2) == 2
assert max_profit([3, 2, 6, 5, 0, 3], 2) == 7
assert max_profit([3, 3, 5, 0, 0, 3, 1, 4], 2) == 6
