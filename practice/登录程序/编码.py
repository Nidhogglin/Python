#!usr/bin/env python3
# coding: utf-8
# @time :2020/10/19 19:15

import base64

with open('./image/icon.ico', 'rb') as icon:
    b64str = base64.b64encode(icon.read())

with open('title.ico', 'wb+') as f:
    f.write(base64.b64decode(b64str))
