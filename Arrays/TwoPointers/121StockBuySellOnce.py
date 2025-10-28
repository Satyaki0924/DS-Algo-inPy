
"""
Problem 121: Best Time to Buy and Sell Stock I (single transaction)
Given an array `prices` where prices[i] is the price of a given stock on the i-th day,
return the maximum profit you can achieve from one buy and one sell. If no profit is possible, return 0.

Approach (two-pointer / scan for minimum):
 - Maintain an index for the day to buy (lowest seen price so far).
 - For each day treated as a potential selling day, compute profit = sell_price - buy_price.
 - Track the maximum profit seen. If current profit is non-positive, update the buy index to the current day (new candidate minimum).
This file contains a short, readable implementation and two example runs at the bottom.
"""

# Define the function to compute maximum profit from a single buy/sell
def findMaxProfit(prices: list) -> int:
    # index of day to buy (start at 0)
    buy = 0; sell = 0; n = len(prices)
    # stores the best profit found so far
    max_profit = 0
    # iterate over every day as potential selling day
    for sell in range(n):
        # price at the current buy index
        buy_price = prices[buy]
        # price at the current sell index
        sell_price = prices[sell]
        # profit if we bought at 'buy' and sold at 'sell'
        profit = sell_price - buy_price
        # update max_profit if this profit is better
        max_profit = max(max_profit, profit)
        # if profit is not positive, the current 'sell' day is a new candidate for the lowest price
        if profit <= 0:
            # move buy pointer to current day (we'll consider buying here going forward)
            buy = sell
    # return the best profit found (0 if no profitable transaction exists)
    return max_profit


# Example 1: there is a profitable transaction (buy at 1, sell at 6 -> profit 5)
prices = [7, 1, 5, 3, 6, 4]
print(findMaxProfit(prices))

# Example 2: prices always go down, so no profit is possible -> returns 0
prices = [7, 6, 4, 3, 1]
print(findMaxProfit(prices))

# Time complexity: O(n) where n is the number of days (single pass through prices). 
# Space complexity: O(1) since we use only a fixed amount of extra space.