class Data:
    def __init__(self):
        self.list1 = [33, 22, 44, 55, 66]

    def change_list(self, index, num):
        self.list1[index] = num

    def sort_list(self):
        return self.list1.sort()

    def insort_list(self):
        print(type(self.list1.sort()))
        return self.list1.sort(reverse=True)

data1 = Data()
data1.list1[0] = 100
print(data1.list1)

data2 = Data()
data2.change_list(0, 100)
print(data2.list1)


data3 = Data()
data3.sort_list()
print(data3.list1)
print(type(data3.list1))

data4 = Data()
data4.insort_list()
print(data4.list1)