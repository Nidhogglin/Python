# coding: utf-8

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
        # 通过在变量前加'__'把变量变为私有变量。外部无法直接访问
        # 实际上变量是被python解释器改成了别的名字，如"_Student__gender"

    # 可以通过内建方法来获取和改变私有变量的值，
    def get_gender(self):
        return self.__gender

    # 设置值时可以增加条件，对参数做检查，避免传入无效的参数
    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            print('bad gender')


if __name__ == '__main__':
    lin = Student('lIN', 'male')
    print(lin.get_gender())
    lin.set_gender('man')  # 设置失败，结果输出'bad gender'

