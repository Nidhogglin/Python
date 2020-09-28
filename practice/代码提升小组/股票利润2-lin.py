#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/27 10:01

def max_profit(prices):
    max_p = 0
    for i in range(len(prices)-1):
        max_p += max(0, prices[i+1]-prices[i])
    return max_p
    
  
def max_profit2(prices):
    max_p = 0
    buy_p = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < prices[i-1]:
            if prices[i-1] > buy_p:
                max_p += prices[i-1] - buy_p
            buy_p = prices[i]
    if prices[-1] > buy_p:
        max_p += prices[-1] - buy_p
    return max_p


def max_profit3(prices):
    max_p = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            max_p += (prices[i+1] - prices[i])
    return max_p
        

if __name__ == '__main__':
    prices = [1,4,3,4,5]
    print(max_profit(prices))
    print(max_profit2(prices))
    print(max_profit3(prices))
