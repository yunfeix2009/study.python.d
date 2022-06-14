def upper_attr(class_name, class_parents, class_attr):
    newdic = {}
    for key,value in class_attr.items():
        if not key.startswith("__"):
            newdic[key.upper()] = value
    return type(class_name,class_parents,newdic)

class A(metaclass=upper_attr):
    num = 100
    def run(self):
        print("run")

@classmethod
def print_b(self):
    print(self.NUM)


@staticmethod
def print_static():
    print("---haha---")


@classmethod
def print_class(self):
    print(self.NUM)


B = type("B", (A,), { "print_b": print_b,
                     "print_static": print_static,
                     "print_class": print_class})

b = B()
b.print_b()
b.print_static()
b.print_class()