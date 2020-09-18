#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/18 12:51

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter


# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
# 可以验证创建的Point对象是tuple的一种子类：
def namedtuple_demo():
    Piont = namedtuple('Point', ['x', 'y', 'z'])
    p = Piont(1, -2, 3)
    print(p.x, p.y, p.z)
    print(isinstance(p, tuple))
    print(isinstance(p, Piont))


# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
def deque_demo():
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    print(q)


# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
def defaultdict_demo():
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    print(dd['key1'])
    print(dd['key2'])


# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict
def orderdDict_demo():
    d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
    print(d)
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(od)


# Counter是一个简单的计数器，例如，统计字符出现的个数
def count_demo():
    c = Counter()
    for ch in 'programing':
        c[ch] += 1
    print(c)
    c.update('hello')   # 也可以一次性update
    print(c)


if __name__ == '__main__':
    namedtuple_demo()
    deque_demo()
    defaultdict_demo()
    orderdDict_demo()
    count_demo()