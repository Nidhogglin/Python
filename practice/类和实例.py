# coding: utf-8


# 创建类
class Student(object):
    # 类的属性
    name = 'Student'
    ty = 'class'

    # 绑定必填对象属性，该方法的第一个参数永远是self，表示创建的实例本身
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 类的方法，可直接用实例调用，必含参数self
    def get_grade(self):
        if self.score > 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


if __name__ == '__main__':
    Lin = Student('Lin', 76)  # 创建实例
    QQ = Student('LQQ', 95)
    print(Lin.name, Lin.get_grade())
    print(QQ.name, QQ.get_grade())
    Lin.age = 22
    print(Lin.age)  # 创建实例额外属性
    try:
        print(QQ.age)
    except:
        print('QQ无age属性')

    print(Lin.name)  # 对象有的属性读取对象的属性值
    print(Lin.ty)  # 对象没有的属性读取类的属性值
