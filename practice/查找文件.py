#!usr/bin/env python
# coding: utf-8
# @time :2020/9/8 14:10

import os
# key = '操作'


def find(p='.'):
    for i in os.listdir(p):
        if os.path.isfile(os.path.join(p, i)) and key in os.path.splitext(os.path.split(i)[1])[0]:
            file_list.append(os.path.join(p, i))
        if os.path.isdir(i):
            find(os.path.join(p, i))


# def key_in():
#     key = input("输入要搜索的内容：")


# def test():
#     print(os.path.abspath('.'))
#
#
# def find2():
#     for i in os.listdir('.\\test'):
#         if os.path.isfile(os.path.join('.\\test', i)):
#             print(i)


if __name__ == '__main__':
    file_list = []
    key = input("输入要搜索的内容：")
    find()
    print(file_list)
