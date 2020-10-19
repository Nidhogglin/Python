#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/29 16:11
from typing import List
import time


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_p1 = prices[0]
        buy_p2 = float('inf')
        max_p = 0
        a = 0
        b = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                if prices[i] - buy_p1 > a:
                    a = prices[i] - buy_p1
                    if i < len(prices)-1:
                        buy_p2 = prices[i+1]
            else:
                if prices[i] < buy_p1:
                    buy_p1 = prices[i]
                for j in range(i, len(prices)-1):
                    if prices[j + 1] < buy_p2:
                        buy_p2 = prices[j + 1]
                    if prices[j+1] - buy_p2 > b:
                        b = prices[j+1] - buy_p2

                    # if prices[j]-buy_p2 > b:
                    #     b = prices[j] - buy_p2
                    # if prices[j] < buy_p2:
                    #     buy_p2 = prices[j]

            max_p = max(max_p, a+b)
            b = 0


        return max_p


a = Solution()
start = time.time()
al = [2,1,4]
print(a.maxProfit(al))
end = time.time()
print(end - start)