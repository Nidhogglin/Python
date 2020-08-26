
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回。
from functools import reduce


def fx(x):
    print(x * x)
    return x * x


a = map(fx, [1, 3, 5, 7, 9])  # 返回的值为一个迭代器
print(a)
print(list(a))  # 把结果转换成list再输出


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算
def add(x, y):
    return x + y


c = reduce(add, [1, 3, 5, 7, 9])
print(type(c))
print(c)
