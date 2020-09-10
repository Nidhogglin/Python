#!usr/bin/env python
# coding: utf-8
# @time :2020/9/9 19:24

import json


# 要把类序列化为JSON，需要先把类转换为dict
class Student(object):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


def Student2dict(std):
    return {
        'name': std.name,
        'gender': std.gender,
        'age': std.age
    }


# 要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例
def dict2Student(d):
    return Student(d['name'], d['gender'], d['age'])


if __name__ == '__main__':
    s = Student('Lin', 'male', 22)
    print(json.dumps(s, default=Student2dict))
    json_str = '{"name": "Lin", "gender": "male", "age": 22}'
    std = json.loads(json_str, object_hook=dict2Student)
    print(std)
    print(std.name)
