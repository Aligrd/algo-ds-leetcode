# find the maximum profit from price[] witch you but in a i(th) and sell an next days find the maximum profit you can get

judge1 = [7, 1, 4, 9, 1, 11, 2]
judge2 = [2, 4, 9, 1, 11, 22, 2, 44]


# best approach to solve this problem with 2pointer
def bestSolve(prices: list) -> int:
    l, r = 0, 1

    max_profit = 0

    while r < len(prices):
        curr_profit = prices[r] - prices[l]
        if curr_profit < 0:
            l = r
        max_profit = max(max_profit, curr_profit)
        r += 1
    return max_profit


print(bestSolve(judge1))
