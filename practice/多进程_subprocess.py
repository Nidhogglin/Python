#!usr/bin/env python
# coding: utf-8
# @time :2020/9/10 18:58

import subprocess


def demo1():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)


# 需要输入的子进程,可以通过communicate()方法输入
def demo2():
    print('$ nslookuo')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('gbk', errors='ignore'))
    print('Exit code:', p.returncode)


if __name__ == '__main__':
    demo1()
    print('=============')
    demo2()