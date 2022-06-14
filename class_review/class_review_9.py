class Monkey():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner



class Persons():
    def __init__(self, name):
        self.name = name
    def eat(self):
        return 'don\'t eat any more!!'


mike = Persons("mike")
mikeMonkey = Monkey("goldenMonkey", mike)
print(mikeMonkey.owner.name)
print(mikeMonkey.name)
print(mikeMonkey.owner.eat())
