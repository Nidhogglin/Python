#!usr/bin/env python3
# coding: utf-8
# @time :2020/11/3 15:55

from wsgiref.simple_server import make_server
from hello import application

# 创建服务器：域名、端口、处理函数
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()