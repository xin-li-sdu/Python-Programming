def pi_(a): #蒙特卡罗方法计算圆周率近似值
    from random import random
    n=0
    for i in range(a):
        x=random()
        y=random()
        if(x*x+y*y<1):
            n=n+1
    print("{:.10f}".format(4*n/a))
b=input('请输入扔飞镖的次数：')
pi_(int(b))