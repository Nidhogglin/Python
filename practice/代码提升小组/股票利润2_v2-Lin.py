#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/27 19:03

"""
题目：
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""


def max_profit2(prices):
    max_p = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_p += (prices[i] - prices[i-1])
    return max_p


if __name__ == '__main__':
    prices = [5,4,3,1,5,4,8]
    print(max_profit2(prices))