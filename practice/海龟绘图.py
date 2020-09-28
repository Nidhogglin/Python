#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/27 19:17

from turtle import *


def demo1():

    width(4)

    forward(200)
    right(90)

    pencolor('red')
    forward(100)
    right(90)

    pencolor('blue')
    forward(200)
    right(90)

    pencolor('yellow')
    forward(100)
    # right(90)

    # done()


def demo2(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)


if __name__ == '__main__':
    for i in range(4):
        demo1()
    done()
    # for x in range(0, 250, 50):
    #     demo2(x, 0)