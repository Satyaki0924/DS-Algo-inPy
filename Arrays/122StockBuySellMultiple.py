
# Problem: Best Time to Buy and Sell Stock II (LeetCode 122)
# You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# However, you must sell the stock before you buy again. Given a list of daily prices, compute the maximum profit.
#
# Easy explanation with example:
# prices = [7,1,5,3,6,4]
# You can buy at 1 and sell at 5 (profit 4), then buy at 3 and sell at 6 (profit 3), total = 7.
# The greedy approach is to sum all positive differences between consecutive days.


# Return the maximum profit obtainable by performing as many buy/sell transactions as desired.
def findMaxProfit(prices: list):
    # Accumulator for total profit across all profitable trades.
    profit = 0
    # If there are fewer than 2 days, no transaction is possible.
    if len(prices) <= 1:
        return profit
    # Iterate through days comparing each day to the previous; capture all positive gains.
    for i in range(1, len(prices)):
        # Current day's price.
        price = prices[i]
        # Previous day's price.
        last_day_price = prices[i-1]
        # If today's price is higher than yesterday's, we can profit by buying yesterday and selling today.
        if price > last_day_price:
            # Add the positive difference to the running profit total.
            profit += price - last_day_price
    # After scanning all days, return the accumulated profit.
    return profit


# --- Example usage ---
prices = [7,1,5,3,6,4]
# Expect 7
print(findMaxProfit(prices))

prices = [7,6,4,3,1]
# Expect 0 (prices strictly decreasing, no profitable trades)
print(findMaxProfit(prices))

# Time complexity: O(n) where n is the number of days (single pass through prices).
# Space complexity: O(1) since we use only a fixed amount of extra space.