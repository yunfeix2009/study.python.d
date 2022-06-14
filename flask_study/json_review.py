import json

# import son as son

dict = {'a': 'wo', 'b': 'zai', 'c': 'zhe', 'd': 'li'}
string = json.dumps(dict)
print(dict)
print(string)
print(type(dict))
print(type(string))

# son.load()

loads = json.loads(string)
print(loads)
print(type(loads))
print(loads['d'])

dict = {'a': 'wo', 'b': 'zai', 'c': 'zhe', 'd': 'li'}
json.dump(dict, open(r'../test.json', 'w'))
jsObj = json.load(open(r'../test.json'))
print(jsObj)
print(type(jsObj))
print(jsObj['a'])