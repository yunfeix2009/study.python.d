# 判断一个数是否是质数.加强版

HM=0
while True:
    try:
        num=int(input('请输入一个数，这里可以判断他是不是质数。\n'))
        if num==0 or num<0:
            print('请输入一个大于零的数。')
            print(' ')
        elif num==1:
            print('不是质数，也不是合数。')
            break
        else:
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    print(num,'是合数')
                    HM += 1
                    break

            else:
                print(num,'是质数')


    except:
        print('输入不正确。')
        print('请正确输入。')
