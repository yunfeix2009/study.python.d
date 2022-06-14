

def func(num1,num2):
    try:
        # 把可能出现异常的代码放到try里面
        res=num1 / num2
        print(res)
    except:
        # 如果出现异常，则执行except
        print("出现异常了")
func(2,1)

# 打印异常
def func(num1,num2):
    try:
        res=num1 % num2
        print(res)
    except Exception as e:
        print(e)
func(2,0)



# try except 捕获指定异常
try:
    print(num)
except NameError:
    print('产生错误了')



# try except 捕获多个异常
try:
    open('123.txt','r')
    print(num)
except(IOError,NameError):
    print("出现了错误")


try:
    # num=100
    print(num)
except NameError as e:
    print('产生错误了:%s'%e)
else:
    print('没有捕获到异常，真高兴')
finally:
    print("我不管，有没有异常我必须执行")