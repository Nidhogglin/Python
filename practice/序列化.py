#!usr/bin/env python
# coding: utf-8
# @time :2020/9/9 16:24

import pickle


# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
def demo1():
    d = dict(name='Lin', gender='male', age='22')
    print(pickle.dumps(d))
    with open('序列化.txt', 'wb') as f:
        f.write(pickle.dumps(d))


# 用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
def demo2():
    d = dict(name='Lqq', gender='female', age='22')
    with open('序列化.txt', 'wb') as f:
        pickle.dump(d, f)


# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
# 也可以用pickle.load()方法从一个file-like Object中直接反序列化出对象

# 反序列化
def demo3():
    with open('序列化.txt', 'rb') as f:
        d = pickle.load(f)
    print(d)


# 反序列化
def demo4():
    with open('序列化.txt', 'rb') as f:
        d = f.read()
    s = pickle.loads(d)
    print(s)


if __name__ == '__main__':
    demo1()
    # demo2()
    demo3()
    demo4()
