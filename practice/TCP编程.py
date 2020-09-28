#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/27 20:37

import socket

def demo1():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.baidu.com', 80))
    s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

    buffer = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)

    s.close()

    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接收的数据写入文件:
    with open('TCP编程_baidu.html', 'wb') as f:
        # f.write(data)
        f.write(html)


if __name__ == '__main__':
    demo1()
