import time
def timer(func): #装饰器函数
    def inner(*args,**kwargs):
        start=time.time()
        re=func(*args,**kwargs)
        print(time.time()-start)
        return re
    return inner
@timer
def func1(*args,**kwargs):
    sum=0
    for i in range(50000):
        sum=sum+i
func1()
