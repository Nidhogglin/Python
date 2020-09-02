#!/usr/bin/env python
# coding: utf-8

# 方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
class Student(object):
    pass


if __name__ == '__main__':
    s = Student()

    # 给实例绑定属性，只对该实例生效
    s.name = 'lin'

    # 给实例绑定方法，只对该实例生效
    def set_age(self, age):
        self.age = age

    from types import MethodType
    s.set_age = MethodType(set_age, s)
    s.set_age(25)
    print(s.age)

    # 给类绑定方法,对该类所有实例生效
    def set_score(self, score):
        self.score = score

    Student.set_score = set_score

    s.set_score(99)
    print(s.score)
