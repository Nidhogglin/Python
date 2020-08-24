# -*- coding: utf-8 -*-
# n格阶梯，一步爬一个或者两格，求爬梯方案数

count = 0


def path_way(n):
    global count

    if n < 0:
        return

    if n == 0:
        count += 1
        return

    for i in range(1, 3):
        path_way(n-i)


path_way(6)
print(count)



