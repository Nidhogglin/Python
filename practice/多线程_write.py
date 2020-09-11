#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/11 10:21

import pickle
import threading
import time


def write():
    time.sleep(3)
    d = dict(name='Lin', gender='male', age='22')
    with open('多线程_write.txt', 'wb') as f:
        pickle.dump(d, f)
    print(threading.current_thread().name, 'end')


if __name__ == '__main__':
    tw = threading.Thread(target=write, name='writethred')
    tw.start()
    print('end')
