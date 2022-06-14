# 综合练习：模拟购物车

# 设计购物车程序,有如下功能：
# 1启动程序后,让用户输入money(整数),然后打印商品列表
# 2允许用户根据商品编号购买商品
# 3用户选择商品后,检测库存够不够,够就直接扣款,不够就提醒
# 4可输入q退出,退出后打印购物车内商品和余额

# 1准备商品
# 因为商品有多个，所以用列表表示
# 商品列表
product_list=[
    ('iPhone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('zhurou',42)
]

# 2 准备购物车
shopping_list=[]

# 3 输入钱数
money=input("请输入你的钱数（整数）:")
if money.isdigit():
    #转换成int型
    money = int(money)
else:
    print("该输入不是只由数字组成")


while True:
    # 4 显示商品列表
    # 取product_list中商品下标和商品
    for index,item in enumerate(product_list):
        print(index,item)
    #5 输入要购买商品的标号
    user_choice=input("选择要买的商品编号：")
    if user_choice=='a':
        product=input('请输入商品名称')
        price=input('请输入商品价钱')
        if price.isdigit():
            # 转换成int型
            price = int(price)
        else:
            print("该输入不是只由数字组成")
        tu=(product,price)
        product_list.append(tu)
        print(product_list)
    elif user_choice.isdigit():
        user_choice=int(user_choice)
        #判断输入编号
        if 0 <= user_choice < len(product_list):
            p_item=product_list[user_choice]
            #判断商品价格是否小于余额
            if p_item[1]<=money:#买的起
                #商品加入购物车
                shopping_list.append(p_item)
                #余额减少
                money-=p_item[1]
                print("添加了%s到购物车,你的账户余额是%d"%(p_item,money))
            else:#买不起
                print("你的余额只有%d，无法购买"%money)
        else:
            print("商品编号%d不存在"%user_choice)
    elif user_choice == "q":
        #退出并显示购物车信息
        print("购物车信息：",shopping_list)
        print("当前余额：",money)
        break
    else:
        print("该输入不是只由数字组成")     



# 课后作业
# 请为购物车的商品列表添加商品。
# 当输入字母"a"时，接着输入商品名称和商品价格