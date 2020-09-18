#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/18 14:45

import struct


# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
# struct的pack函数把任意数据类型变成bytes：
def pack_demo():
    # pack的第一个参数是处理指令，'>I'的意思是：
    # > 表示字节顺序是big - endian，也就是网络序，I表示4字节无符号整数。
    # 后面的参数个数要和处理指令一致。
    print(struct.pack('>I', 10240099))


# unpack把bytes变成相应的数据类型
def unpack_demo():
    # 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
    # 所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。
    print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))


# 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。


if __name__ == '__main__':
    pack_demo()
    unpack_demo()