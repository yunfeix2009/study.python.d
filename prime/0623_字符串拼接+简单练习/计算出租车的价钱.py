length=int(input('请输入您的公里数'))
if length<=3:
    print('请支付13块钱')
else :
    print('请支付',(length-3)*2+13,'块钱')