#内部生成器
def ave1():
    i = []
    s,l=0,0
    i=yield []
    while len(i)!=0:
        s+=sum(i)
        l+=len(i)
        i = yield s/l
#外部生成器        
def ave2():
    yield from ave1()
#实例化
gen=ave2()
next(gen)
while(True):
    numlist=list(input('请进行下一轮输入或者回车结束进程：').split(' '))
    #判断结束条件
    if numlist==['']:
        break
    #类型转换
    for i in range(len(numlist)):
        numlist[i]=int(numlist[i])
    print(gen.send(numlist))
