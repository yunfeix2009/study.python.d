import re

'''
python 3.5版本
正则匹配中文，固定形式：\u4E00-\u9FA5
'''

initially_str = 'not 404 found 张三 99深圳'
re_str = re.compile("[\u4E00-\u9FA5]+")
match_obj = re.findall(re_str, initially_str)
str_print=match_obj[0]
print(' '.join(match_obj))