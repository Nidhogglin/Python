#!usr/bin/env python
# coding: utf-8
# @time :2020/9/10 16:52

from multiprocessing import Process, Pool
import os, time, random


# demo1子进程需要执行的代码
def run_proc(name):
    print('run child process %s %s, my parent is %s' % (name, os.getpid(), os.getppid()))


def demo1():
    print('parent process %s ' % os.getpid())

    # 创建子进程，参数：子进程需要执行的函数，需要传入的参数，创建一个process实例
    p = Process(target=run_proc, args=('test',))
    print('child process will start')
    # 启动子进程
    p.start()
    # 等待子进程结束再往下运行，通常用于进程间的同步
    p.join()
    print('child process end')


# demo2子进程需要执行的代码
def long_time_task(name):
    print('child process %s(%s, parent(%s)) start running' % (name, os.getpid(), os.getppid()))
    start_time = time.time()
    time.sleep(random.random() * 5)
    end_time = time.time()
    print('child process %s(%s) end, tacks %.2f seconds' % (name, os.getpid(), end_time-start_time))


# 用进程池的方法批量创建子进程
def demo2():
    print('parent process %s' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))
    print('waiting for all subprocesses done...')
    # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
    # 调用close()之后就不能继续添加新的Process了。
    p.close()
    p.join()
    print('all subprocesses done')


if __name__ == '__main__':
    demo1()
    print('======')
    demo2()