class cesi(object):
    """这是一个用于测试的类"""

    def __init__(self, name, age):
        print('init has be called')
        # super(cesi, self).__init__()
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print('new has be called')
        return object.__new__(cls)


    def set_name(self):
        self.name = "Tom"

class cesi_2(cesi):
    def __new__(cls):
        print('new has be called')
        return super().__new__(cls)
    def __init__(self):
        print('init has be called')

if __name__ == "__main__":
    t = cesi_2()
    # print(t.name)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     __format_dict = {
#         'n-a': '名字是：{obj.name}-年龄是：{obj.age}',  # 名字是：maple-年龄是：18
#         'n:a': '名字是：{obj.name}：年龄是：{obj.age}',  # 名字是：maple：年龄是：18
#         'n/a': '名字是：{obj.name}/年龄是：{obj.age}',  # 名字是：/年龄是：18
#     }
#
#     def __format__(self, format_spec):
#         if not format_spec or format_spec not in self.__format_dict:
#             format_spec = 'n-a'
#         fmt = self.__format_dict[format_spec]
#         print(fmt) #{obj.name}:{obj.age}
#         return fmt.format(obj=self)
#
# s1 = Student('maple', 24)
# ret = format(s1, 'n/a')
# print(ret)  # maple/24