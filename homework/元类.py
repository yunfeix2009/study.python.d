def upper_attr(a,b,c):
    d = {}
    for i in c.keys():
        if not i.startswith("__"):
            d[i.upper()] = c[i]
    return type(a,b,d)
class e(metaclass=upper_attr):
    def _1234(self):
        print(1)
    def plus2(self):
        i=2
    def plus3(self):
        i = 3

    def plus4(self):
        i = 4

f=e()
f._1234()
# print(dir(f))