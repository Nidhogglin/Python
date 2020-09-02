# coding： utf-8

class Myobject(object):
    def __init__(self,):
        self.x = 9

    def power(self):
        return self.x * self.x

    def __len__(self):
        return 100


if __name__ == '__main__':

    obj = Myobject()

    # 查看该对象是否有某属性或方法
    print(hasattr(obj, 'x'))
    print(hasattr(obj, 'y'))
    print(hasattr(obj, 'power'))

    # 获取该对象属性或方法值
    print(getattr(obj, 'x'))
    print(getattr(obj, 'power'))
    print(getattr(obj, 'y', 404))  # 如果存在，返回y的值，若存在，返回默认值404

    # 设置属性值
    setattr(obj, 'y', 19)
    print(getattr(obj, 'y'))   # ==》print(obj.y)

    # 获取对象所有属性和方法
    print(dir(obj))
    print(len(obj))  # ==> print(obj.__len__())
    print(obj.__len__())


