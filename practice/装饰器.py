# coding: utf-8

import functools
import time


# def log1(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         return func(*args, **kw)
#     print('call %s:' % func.__name__)
#     return wrapper
#
#
# @log1
# def now1():
#     print("2020-9-1")


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s %s' % (func.__name__, text))
            return func(*args, **kw)
        return wrapper
    return decorator


@log2('哈哈哈')
def now2():
    print('2020-9-1')


def log3(*args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args1, **kw):
            if isinstance(args[0], str):
                print("%s%s():" % (args[0], func.__name__))
            else:
                print("%s():" % func.__name__)
            return func(*args1, **kw)
        return wrapper
    if isinstance(args[0], str):
        return decorator
    return decorator(args[0])


@log3('执行')
def now3():
    print('20200901')


@log3
def now4():
    print('2020-09-01')


def metric(fn):
    def wrapper(*args, **kw):
        print('start')
        start_time = time.time()
        print(fn(*args, **kw))
        end_time = time.time()
        print('stop')
        print('%s executed in %s ms' % (fn.__name__, end_time-start_time))
        return fn(*args, **kw)
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


if __name__ == '__main__':
    # now1()
    # print(now1.__name__)
    # now2()
    # fast(11, 22)
    # print(fast(11, 22))
    # print(slow(11, 22, 33))
    now3()
    now4()

