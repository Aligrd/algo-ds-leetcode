# buy and sell stock continiously and return the maximum profit you can earn


#! with 2pointer
def maxProfit(self, prices: list[int]) -> int:
    l, r = 0, 1
    max_profit = 0

    while r < len(prices):
        curr_profit = prices[r] - prices[l]

        if curr_profit > 0:
            max_profit += curr_profit

        l += 1
        r += 1
    return max_profit
