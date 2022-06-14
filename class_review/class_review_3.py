class Student(object):
    name1 = "Tony"
    def __init__(self, name):
        self.name = name

    def eat(self, something):
        print("eat the ", something)

    @staticmethod
    def sleep(b):
        print("static method", b)

    @classmethod
    def goodstudy(cls, a):
        print("class method", a)

    @classmethod
    def setName(cls, name):
        print("class method")
        cls.name1 = name


if __name__ == '__main__':
    stud = Student("tom")
    stud.eat('pizza')
    stud.name1 = "lucy"
    print(stud.name1)
    stud.setName("abc")
    print(stud.name1)
    stud.goodstudy('a')
    Student.goodstudy('a')
    stud.sleep('b')
    Student.sleep('b')

    # t = Student(Student.name1)
    # print(t.name1)
    # print(t.name)