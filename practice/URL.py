#!/usr/bin/env python
# coding: utf-8

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, *args, **kwargs):
        return Chain('%s/%s' % (self._path, args[0]))

    __repr__ = __str__


if __name__ == '__main__':
    path1 = Chain().user.status.timeline.list
    path2 = Chain().users('Lin').repos
    print(path1)
    print(path2)

