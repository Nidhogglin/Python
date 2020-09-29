#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/28 15:22

import socket

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(('127.0.0.1', 9999))

# 接受欢迎消息
print(s.recv(1024).decode('utf-8'))

for data in [b'Michael', b'Lin', b'Lqq']:
    # 发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
