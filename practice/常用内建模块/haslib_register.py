#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/18 15:17

from datetime import datetime
import hashlib
import json
import os


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


# 注册练习
def register():
    print('欢迎注册')
    username = input('输入用户名：')

    while is_exist(username):
        print('用户已存在,请选择别的用户名')
        username = input('输入用户名：')

    password = input('请输入密码：')
    password2 = input("请确认密码：")

    while password2 != password:
        print('两次密码不一致，请再次输入')
        password = input('请输入密码：')
        password2 = input("请确认密码：")

    user = dict([
        ('create_time', str(datetime.now())),
        ('username', username),
        ('password', password_encode(username+password))
    ])
    with open('users.txt', 'a') as f:
        json.dump(user, f)
        f.write('\n')
    print('注册成功')


if __name__ == '__main__':
    register()
    # is_exist('lin')
    # print(is_exist('lin'))