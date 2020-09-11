#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/11 10:57

import threading
import multiprocessing


def loop():
    x = 0
    while True:
        x ^= 1


if __name__ == '__main__':
    for i in range(multiprocessing.cpu_count()):
        lt = threading.Thread(target=loop, name='loopthred')
        lt.start()