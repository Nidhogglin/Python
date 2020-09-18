#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/18 17:17

import hmac


def demo1():
    print(hmac.new(b'123', b'123456', 'MD5').hexdigest())
    key = '123'
    password = '123456'
    print(hmac.new(key.encode('utf-8'), password.encode('utf-8'), 'MD5').hexdigest())


if __name__ == '__main__':
    demo1()