#!/usr/bin/env python
# coding: utf-8

from io import StringIO


def demo1():
    f = StringIO()
    f.write('Hello')
    f.write(',')
    print(f.write('world!'))  # 写入操作，打印的是写入字符数
    print(f.getvalue())


def demo2():
    f = StringIO("Hello!\nHi!\nGoodbye!")
    for i in f.readlines():
        print(i.strip())  # strip()：移除字符串首尾的指定字符（默认为空格或换行符）或字符序列


if __name__ == '__main__':
    demo1()
    demo2()
