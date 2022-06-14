class my_pocket(object):
    def __init__(self):
        self.__money = 20
    @property
    def money(self):
        return self.__money
    # @money.setter
    def money(self,money):
        if isinstance(money,int):
            self.__money = money
        else:
            print('密码不对！！！！')

p1 = my_pocket()
p1.money= 100000
print(p1.money)