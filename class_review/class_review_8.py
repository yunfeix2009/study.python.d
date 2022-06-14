class Animals(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating")


class Cat(Animals):
    def __init__(self, name):
        super(Cat, self).__init__(name)


class Pig(Animals):
    def __init__(self, name):
        super(Pig, self).__init__(name)


class Person():
    def feedAnimal(self, animal):
        animal.eat()


cat = Cat("tom")
pig = Pig("peiqi")
tony = Person()
tony.feedAnimal(cat)
tony.feedAnimal(pig)
