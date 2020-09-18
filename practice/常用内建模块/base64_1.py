#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/18 14:11

import base64
import pickle


def demo1():
    b1 = base64.b64encode(b'binary\x00string')
    print(b1)
    print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

    # 由于标准的Base64编码后可能出现字符 + 和 /，在URL中就不能直接作为参数，所以又有一种
    # "url safe"的base64编码，其实就是把字符 + 和 / 分别变成 - 和_
    print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    print(base64.urlsafe_b64decode(b'abcd--__'))


# 练习
# 请写一能处理去掉=的base64解码函数
def safe_base64_decode(s):
    for i in range(4 - len(s) % 4):
        if isinstance(s, bytes):
            s += b'='
        else:
            s += '='
    return base64.b64decode(s)


if __name__ == '__main__':
    demo1()
    print(safe_base64_decode(b'YWJjZA'))
    print(safe_base64_decode('YWJjZA=='))
