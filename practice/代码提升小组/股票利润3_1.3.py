#!usr/bin/env python3
# coding: utf-8
# @time :2020/10/12 15:15
from typing import List
import time


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_p1, buy_p2 = float('inf'), float('inf')
        max_p1, max_p2 = 0, 0
        for i in prices:
            buy_p1 = min(i, buy_p1)
            max_p1 = max(max_p1, i-buy_p1)
            buy_p2 = min(buy_p2, i-max_p1)
            max_p2 = max(max_p2, i-buy_p2)

        return max_p2


s = Solution()
a = s.maxProfit([8,3,6,2,8,8,8,4,2,0,7,2,9,4,9])
print(a)

