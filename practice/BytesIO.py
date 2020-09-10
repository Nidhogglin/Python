#!/usr/bin/env python
# coding: utf-8

from io import BytesIO


def demo1():
    f = BytesIO()
    print(f.write("中文".encode('utf-8')))  # 打印的是字节数
    print(f.getvalue())


def demo2():
    f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    print(f.read())


if __name__ == '__main__':
    demo1()
    demo2()
