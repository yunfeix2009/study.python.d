# from collections import Iterator
#
# x = isinstance([11, 22, 33, 44], Iterator)
# print(x)

from collections.abc import Iterable
from collections.abc import Iterator


class person(object):
    def __init__(self):
        self.name = list()
        self.current_num = 0

    def add(self, name):
        self.name.append(name)

    def __iter__(self):
        return [11, 22, 33].__iter__()


def main():
    zzy = person()
    print("Whether the object can be iterated: {}".format(isinstance(zzy, Iterable)))
    for i in zzy:
        print(i)


if __name__ == '__main__':
    main()

import time
from collections.abc import Iterable
from collections.abc import Iterator


class person(object):
    def __init__(self):
        self.name = list()
        self.current_num = 0

    def add(self, name):
        self.name.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.name):
            ret = self.name[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration

def main():
    zzy = person()
    print("Whether the object can be iterated: {}".format(isinstance(zzy, Iterator)))
    zzy.add("Jhon")
    zzy.add("yinxiaohui")
    zzy.add("DD")
    for i in zzy:
        print(i)

if __name__ == '__main__':
    main()