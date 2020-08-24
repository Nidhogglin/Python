# -*- coding: utf-8 -*-
# n格阶梯，一步爬一个或者两格，求爬梯方案数

count = 0


def path_way(n, step=2):

    global count

    if n < 0:
        return

    if n == 0:
        count += 1
        return

    for i in range(1, step+1):
        path_way(n-i)


if __name__ == '__main__':
    n = 10
    path_way(n)
    print(count)



