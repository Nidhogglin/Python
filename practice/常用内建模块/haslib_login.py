#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/18 16:16

import json
import os
import hashlib


def password_encode(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


def is_exist(username):
    if os.path.exists('users.txt'):
        with open('users.txt', 'r') as f:
            for line in f.readlines():
                user = dict(json.loads(line))
                # print(user)
                if username == user['username']:
                    return True
        return False
    else:
        return False


def is_corect(username, password):
    with open('users.txt', 'r') as f:
        for line in f.readlines():
            user = dict(json.loads(line))
            # print(user)
            if username == user['username']:
                if password == user['password']:
                    return True
                else:
                    return False
            else:
                continue


def login():
    print('欢迎登录')
    username = input('请输入用户名：')
    password = input("请输入密码：")

    while not is_exist(username):
        print('用户不存在')
        username = input('请输入用户名：')
        password = input("请输入密码：")

    for i in range(3):
        md5_str = password_encode(username+password)
        # print(md5_str)
        if is_corect(username, md5_str):
            print('登录成功')
            break
        elif i < 2:
            print('密码错误，你还有%d次机会' % (2-i))
            password = input("请输入密码：")
        else:
            print('你已错误三次，账号将被锁定')


if __name__ == '__main__':
    login()