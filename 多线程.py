#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/10 20:51

import threading, time


def loop():
    print(threading.current_thread().name+'is running...')
    for i in range(5):
        print(threading.current_thread().name+'>>>', i)
        time.sleep(1)


if __name__ == '__main__':
    print(threading.current_thread().name)
    t = threading.Thread(target=loop, name='loopthred')
    t.start()
    t.join()