class Person:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


if __name__ == '__main__':
    p1 = Person('tom', 11, 1000)
    print(p1.get_age())
    p1.set_age(100)
    print(p1.get_age())

    print(p1.age)
    p1.age = 28
    print(p1.age)