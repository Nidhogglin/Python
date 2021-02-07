#!usr/bin/env python3
# coding: utf-8
# @time :2020/11/9 11:46

def demo1(a):
    b = []
    for i in a:
        isP = 1
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                isP = 0
                break
        if isP:
            b.append(i)
    return b


if __name__ == '__main__':
    a = [i for i in range(10, 101)]
    print(demo1(a))