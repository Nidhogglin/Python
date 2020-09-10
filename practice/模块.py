#!/usr/bin/env python
# coding: utf-8

"""this is a test module"""

__author__ = 'Nidhogg Lin'

import sys


def hello():
    args = sys.argv
    if len(args) == 1:
        print("Hello, World!")
    elif len(args) == 2:
        print("Hello, %s" % args[1])
    else:
        print("too much arguments!")


if __name__ == '__main__':
    hello()
