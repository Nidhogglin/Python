#!usr/bin/env python
# coding: utf-8
# @time :2020/9/9 18:15

import json


# dumps()方法返回一个str，内容就是标准的JSON
def demo1():
    d =dict(name='Lin', gender='male', age='22')
    print(d)
    print(json.dumps(d))


# dump()方法可以直接把JSON写入一个file-like Object
def demo2():
    d = dict(name='Lqq', gender='female', age='22')
    with open('JSON序列化.txt', 'w') as f:
        json.dump(d, f)


# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
def demo3():
    with open('JSON序列化.txt', 'r') as f:
        d = json.load(f)
        f.seek(0)
        json_str = f.read()
    print(d)
    print(json.loads(json_str))


if __name__ == '__main__':
    demo1()
    demo2()
    demo3()