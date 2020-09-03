#!/usr/bin/env python
# coding: utf-8

# __slots__可以对当前类的实例绑定属性进行限制，但不能限制子类的实例
class Student(object):
    __slots__ = ('name', 'age')


class Boy(Student):
    pass


class Girl(Student):
    __slots__ = ('birth',)


if __name__ == '__main__':
    s = Student()
    s.name = 'Lin'
    s.age = '22'
    try:
        s.score = 99
    except:
        print('不能设置限制以外的属性')
    b = Boy()
    b.score = 99
    print(b.score)
    g = Girl()
    g.name = 'Lqq'
    g.age = '22'
    g.birth = '1998'
    try:
        g.score = 99
    except:
        print('子类只能设置子类限制+父类限制范围内的值')
