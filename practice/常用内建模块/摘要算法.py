#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/17 10:20

import hashlib


def md5demo1():
    md5 = hashlib.md5()
    username = 'lin'
    password = 'hf123456'
    str1 = username + password
    print(str1)
    md5.update(str1.encode('utf-8'))
    print(md5.hexdigest())


def md5demo2():
    md5 = hashlib.md5()
    username = 'lin'
    password = 'hf123456'
    md5.update(username.encode('utf-8'))
    md5.update(password.encode('utf-8'))
    print(md5.hexdigest())


def sha1demo():
    sha1 = hashlib.sha1()
    password = 'hf123456'
    sha1.update(password.encode('utf-8'))
    print(sha1.hexdigest())


if __name__ == '__main__':
    md5demo1()
    md5demo2()
    sha1demo()
