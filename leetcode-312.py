# burst ballons to give maximum coins

import random
import math


def burstBalloons(nums: list) -> int:
    nums = [1] + nums + [1]
    dpCache = {}

    def dfs(l, r):
        if l > r:
            return 0

        if (l, r) in dpCache:
            return dpCache[(l, r)]

        dpCache[(l, r)] = 0

        for i in range(l, r + 1):
            coins = nums[l - 1] * nums[i] * nums[r + 1]
            coins += dfs(l, i - 1) + dfs(i + 1, r)
            dpCache[(l, r)] = max(dpCache[(l, r)], coins)
        return dpCache[(l, r)]

    return dfs(1, len(nums) - 2)

#! I DIDNT FUCKING KNOW ANYTHING

# def MinIndex(list: list) -> int:
#     minIndex = 0
#     for i in range(len(list)):
#         if list[i] < list[minIndex]:
#             minIndex = i
#     return minIndex


lir = [3, 1, 5, 8]
res = burstBalloons(lir)
print(res)
