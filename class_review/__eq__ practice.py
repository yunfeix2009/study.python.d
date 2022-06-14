class A(object):
    def __init__(self, name, x):
        self.name = name
        self.x = x

    def __repr__(self):
    	return self.name

    def __str__(self):
    	return "I'am right"

    def __eq__(self, obj):
    	if self.name == obj.name :
    		return True
    	else:
    		return False


a = A('zzy', 6)
b = A('zzy', 7)
print(str(a))
print(a == b)