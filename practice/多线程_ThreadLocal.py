#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/11 15:00

import threading


def process_student():
    std = local_school.student
    print('hello, %s(in %s)' %(std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


if __name__ == '__main__':
    local_school = threading.local()
    t1 = threading.Thread(target=process_thread, args=('Alex',), name='t1')
    t2 = threading.Thread(target=process_thread, args=('Lin',), name='t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
