def login(func):
    def inner_func(*args):
        """需要实现:
        1.显示欢迎内容,比如:欢迎您使用check_prim函数,请登录后使用  ok
        2.让用户输入用户名和密码 ok
        3.从database.txt检查用户名和密码是否正确
        4.正确则可以正常使用函数
        5.装饰器需要保留原函数名和原函数的帮助文档
        """
        print('欢迎使用{}函数'.format(func.__name__))
        print('请登录后使用')
        uesername = input('请输入用户名')
        password = input('请输入密码')
        if username_password_dict.keys().__contains__(uesername) and username_password_dict[uesername] == password:
            return func(*args)
        else:
            return None
    return inner_func

@login
def check_prim(n: int):
    """
    输入整数,判断其是否是质数
    """

    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if not n % i:
            return False
    return True

@login
def my_int_power(a: int, b: int):
    """
    输入两个整数
    """

    power = 1
    if a == 0:
        return 0
    for i in range(b):
        power *= a
    return power

number = 10
a, b = 2, 3
flage = True
# init username_password_dict
username_password_dict = {}
with open('database.txt', 'r', encoding='utf-8') as f:
    rls = f.readlines()
for item in rls[1:]:
    username_password_ls = item.rstrip().split('\t')
    username_password_dict[username_password_ls[0]] = username_password_ls[1]
while flage:
    anser1 = check_prim(number)
    if anser1 is None:
        print("登陆失败,请重新输入登录信息\n")
    else:
        print("{}是否是质数:".format(number), "是" if anser1 else "否")
        flage = False

flage = True

if b > 0:
    while flage:
        anser2 = my_int_power(a, b)
        if anser2 is None:
            print("登陆失败,请重新输入登录信息\n")
        else:
            print("{}的{}次幂是{}".format(a, b, anser2))
            flage = False
else:
    print("幂数必须为非负整数")