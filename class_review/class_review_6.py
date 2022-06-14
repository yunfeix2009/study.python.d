import abc


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod  # 抽象的对象方法
    def sound(self):
        pass

    @abc.abstractclassmethod  # 抽象的类方法
    def test1(cls):
        pass

    @abc.abstractstaticmethod  # 抽象的静态方法
    def test2(self):
        pass

class Dog(Animal):
    def sound(self):
        print("wang wang")

    @classmethod
    def test1(cls):
        print("class of method")

    @staticmethod
    def test2():
        print("static of method")


dog = Dog()
dog.sound()
dog.test1()
Dog.test1()
dog.test2()
Dog.test2()
