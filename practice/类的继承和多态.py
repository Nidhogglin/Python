# 实例的数据类型就是类或父类的名称

class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):  # Dog是Animal的子类
    def run(self):
        print('Dog is running')


class Cat(Animal):
    def run(self):
        print('Cat is running')


def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':
    a = Animal()
    b = Dog()
    c = Cat()
    a.run()
    b.run()
    c.run()
    print(type(a))
    print(isinstance(c, Cat))
    print(isinstance(c, Animal))
    print(isinstance(a, Cat))

    # 当子类和父类有同名方法时，子类使用自己的方法
    run_twice(Animal())
    run_twice(Dog())
    run_twice(Cat())
