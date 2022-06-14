import abc


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod  # 抽象的对象方法
    def sound(self):
        pass

    # @abc.abstractclassmethod  # 抽象的类方法
    # def test1(cls):
    #     pass
    #
    # @abc.abstractstaticmethod  # 抽象的静态方法
    # def test2(self):
    #     pass

class dog(Animal):
    def sound1(self):
        print("o")

    def sound(self):
        print("o")

if __name__ == '__main__':
    Tom = dog()
    Tom.sound1()