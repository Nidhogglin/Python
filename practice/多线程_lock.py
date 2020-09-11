#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/11 11:05

import threading


# 不上锁时，修改balance需要多条语句，而执行这几条语句时，
# 线程可能中断，从而导致多个线程把同一个对象的内容改乱了
def run_thread_unlock(n):
    global balance_unlock
    for i in range(2000000):
        balance_unlock += n
        balance_unlock -= n


# 线程获得锁后，其他线程不能同时执行锁内的语句，只能等待到锁被释放后，获得该锁以后才能执行
# 由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。
def run_thread_lock(n):
    global balance_lock
    for i in range(2000000):
        # 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。
        # 所以我们用try...finally来确保锁一定会被释放
        lock.acquire()
        try:
            balance_lock += n
            balance_lock -= n
        finally:
            lock.release()


def unlock():
    t1 = threading.Thread(target=run_thread_unlock, args=(5,), name='unlookThred1')
    t2 = threading.Thread(target=run_thread_unlock, args=(8,), name='unlookThred2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('unlock result:', balance_unlock)


def locked():
    t1 = threading.Thread(target=run_thread_lock, args=(5,), name='unlookThred1')
    t2 = threading.Thread(target=run_thread_lock, args=(8,), name='unlookThred2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('lock result:', balance_lock)


if __name__ == '__main__':
    # 创建一个锁就是通过threading.Lock()来实现
    lock = threading.Lock()
    balance_unlock, balance_lock = 0, 0
    unlock()
    locked()
