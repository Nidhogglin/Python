#!usr/bin/env python3
# coding: utf-8
# @time :2020/10/10 15:41

class Solution:
    def maxProfit(self, prices) -> int:
        buy_1 = buy_2 = float('inf')  # 第一二次买之前的最低价
        pro_1 = pro_2 = 0

        for p in prices:
            buy_1 = min(buy_1, p)
            pro_1 = max(pro_1, p - buy_1)
            buy_2 = min(buy_2, p - pro_1)  # p - pro_1 是用第一次的钱抵消了一部分第二次买的钱
            pro_2 = max(pro_2, p - buy_2)
        return pro_2


s=Solution()
a = s.maxProfit([8,3,6,2,8,8,8,4,2,0,7,2,9,4,9])
print(a)