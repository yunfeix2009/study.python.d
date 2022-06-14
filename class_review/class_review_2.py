class Student():
    def __init__(self, name, age, sex, class_num, sno):
        self.name = name
        self.age = age
        self.sex = sex
        self.class_num = class_num
        self.sno = sno

    def display_info(self):
        print(self.name, self.age, self.sex, self.class_num, self.sno)

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

if __name__ == '__main__':
    stu_1 = Student('steven', 12, 'male', 21, 21)
    stu_2 = Student('tony', 30, 'male', 1, 2)
    stu_2.set_age(18)
    print(stu_2.get_name())
    stu_1.display_info()
    stu_2.display_info()