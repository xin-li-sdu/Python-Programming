import random
def suiji():  #生成随机密码
    k=list()
    c=list()
    for i in range(1,8):
        a=random.randint(33,126)
        if 47<a<58:
            b=1
        elif 64<a<91:
            b=2
        elif 96<a<123:
            b=3
        else:
            b=4
        if b not in c:
            c.append(b)
        k.append(chr(a))
    k=''.join(k)
    if len(c)>=3:
        print("是强密码：",k)
    else:
        print("不是强密码：",k)
suiji()
