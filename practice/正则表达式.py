#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/11 16:27

import re


def demo1():
    # match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
    # 使用r前缀可以忽略python'\'本身的转义效果
    # 参数：第一个参数为正则表达式， 第二个参数为需要匹配的字符串
    text = '010-12345'
    print(re.match(r'\d{3}\-\d{3,8}', text))

    # 常见的判断方法
    if re.match(r'\d{3}\-\d{3,8}', text):
        print('OK')
    else:
        print('Fail')


def demo2():
    # 切分字符串
    # 正常的切分代码。无法识别连续的空格
    print('a b   c'.split(' '))
    # 无论多少个空格都可以正常分割
    print(re.split(r'\s+', 'a b   c'))

    print(re.split(r'[\s\,]+', 'a,b, c  d'))

    print(re.split(r'[\s\,\;]+', 'a,b;;c,   d'))


# 提取合法时间
def demo3():
    t = '19:29:49'
    m = re.match(r'^([0-1][0-9]|2[0-3]|[0-9])\:([0-5][0-9]|[0-9])\:([0-5][0-9]|[0-9])$', t)
    print(m.groups())
    print(m.group(0))
    print(m.group(1))


# 贪婪匹配
def demo4():
    # 则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
    # 由于\d + 采用贪婪匹配，直接把后面的0全部匹配了，结果0 * 只能匹配空字符串了
    print(re.match(r'^(\d+)(0*)$', '102300').groups())
    # >>>('102300', '')

    # 必须让\d + 采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d + 采用非贪婪匹配：
    print(re.match(r'^(\d+?)(0*)$', '102300').groups())
    # >>>('1023', '00')


def is_valid_email(addr):
    if re.match(r'^([a-zA-Z]+\.?\w+)\@\w+\.\w+$', addr):
        return re.match(r'^([a-zA-Z]+\.?\w+)\@\w+\.\w+$', addr).group(1)
    return


if __name__ == '__main__':
    demo1()
    demo2()
    demo3()
    demo4()
    print(is_valid_email('nidhogg.lin@qq.com'))
    print(is_valid_email('nidhogg-lin@qq.com'))