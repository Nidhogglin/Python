#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/11 20:18


def func(s):

    n = len(s)

    while n > 1:

        char_dict = {}
        for i in s:
            char_dict[i] = 0

        for i in s[:n]:
            char_dict[i] += 1

        char_odd = 0
        for key in char_dict.keys():
            if char_dict[key] % 2 == 1:
                char_odd += 1
            if char_odd == 2:
                break
        if char_odd < 2:
            return s[:n]
        n -= 1


if __name__ == '__main__':
    s = 'aaaassdfgd'
    print(func(s))