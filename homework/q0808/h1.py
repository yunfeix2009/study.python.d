def _0808temp_():
    while True:
        Var=input('请输入一个变量名。 \n')
        if Var=='':
            print('不能为空！')
        else:
            break
    if Var[0].isalpha() or Var[0]=='_':
        for i in Var:
            if i.isalpha() or i=='_' or i.isdigit():
                pass
            else:
                print('不合法。')
                exit()
        print('正确')
    else:
        print('不合法。')
        print('首字母不是字母或数字！')
_0808temp_()