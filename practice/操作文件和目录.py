#!/usr/bin/env python
# coding: utf-8

import os

def osdemo1():

    print(os.name)  # 操作系统名称'nt'表示windows，'posix'表示Linux、Unix或Mac OS X

    # print(os.uname())  获取系统详细信息，windows系统上不提供

    print(os.environ)  # 环境变量
    print(os.environ.get('username'))  # 获取指定环境变量的值


# 操作文件和目录
def osdemo2():
    # 查看当前目录的绝对路径
    print(os.path.abspath('.'))

    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
    os.path.join('E:\\code\\Python', 'testdir')
    # 然后创建一个目录
    os.mkdir('E:\\code\\Python\\testdir')
    # 删除一个目录
    os.rmdir('E:\\code\\Python\\testdir')


def osdemo3():
    fa_path = os.path.abspath('..')
    dir_path = os.path.join(fa_path, 'testdir')
    os.mkdir(dir_path)
    file_path = os.path.join(dir_path, 'file.txt')
    print(file_path)
    with open(file_path, 'a+'):
        pass
    print(os.path.split(dir_path))
    print(os.path.splitext(file_path))
    os.rename(dir_path+'\\file.txt', dir_path+'\\file.py')
    os.remove(dir_path+'\\file.py')
    os.rmdir(dir_path)


def osdemo4():
    # 用列表表示当前文件夹所有的目录
    dir_list = [x for x in os.listdir('.') if os.path.isdir(x)]
    print(dir_list)

    # 用列表表示当前文件夹所有的'.py'后缀的文件
    file_list = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
    print(file_list)


if __name__ == '__main__':
    pass
    # osdemo1()
    # osdemo2()
    # osdemo3()
    osdemo4()