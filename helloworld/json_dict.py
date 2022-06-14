import json
dict_1 = {
"name": "steven",
"gender": "male"
}
# dump1=json.dump(dict_1)
# print(type(dump1))

with open("steven.json","w",encoding="utf-8") as f:
    json.dump(dict_1, f, ensure_ascii=False, indent=2)  ### ensure_ascii=False确保中文正常显示, indent=2可以增加缩进,且缩进为2个空格
    print(type(f))

with open("steven.json","r",encoding="utf-8") as f:
    # print(type(json.load(f)))
    # for line in f.readline():
    #     print(line)
    # print(f.readlines())
    # print(f.readlines())
    # print(f)
    dict_2 = json.load(f)

# print(type(dict_2))
# print(dict_2)
# print(dict_2['name'])