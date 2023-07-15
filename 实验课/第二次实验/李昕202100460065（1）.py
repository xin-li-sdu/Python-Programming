def date(a): #计算第几天
    shuju=a.split('/')
    m=int(shuju[0])
    n=0
    if (m%100==0)&(m%400==0): #判断是否是闰年
        n=1
    elif(m%100!=0)&(m%4==0):
        n=1
    aDict1={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    aDict2={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    i=1
    sum=0
    if n==1:
        while i<int(shuju[1]):
            sum=sum+aDict2[i]
            i=i+1
    else:
        while i<int(shuju[1]):
            sum=sum+aDict1[i]
            i=i+1
    sum=sum+int(shuju[2])
    print(a,'是第',sum,'天')

def date1():
    import time
    a=time.strftime("%Y/%m/%d")
    shuju=a.split('/')
    m=int(shuju[0])
    n=0
    if (m%100==0)&(m%400==0): #判断是否是闰年
        n=1
    elif(m%100!=0)&(m%4==0):
        n=1
    aDict1={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    aDict2={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    i=1
    sum=0
    if n==1:
        while i<int(shuju[1]):
            sum=sum+aDict2[i]
            i=i+1
    else:
        while i<int(shuju[1]):
            sum=sum+aDict1[i]
            i=i+1
    sum=sum+int(shuju[2])
    print('今天是第',sum,'天')
    
a=input('请以/为间隔符输入日期，省略无效的0：')
date(a)
date1()