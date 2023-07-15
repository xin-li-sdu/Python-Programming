import random
print("已经随机生成了一个数字")
num=int(input("设置尝试次数："))
flag=0
k=random.randint(1,100) #生成一个随机数
while num>0:
    a=input("请输入数：")
    num=num-1
    try:
        a=int(a)
    except:
        print("输入格式错误，请重新输入")
        continue
    if a== k:
        print("猜对了！")
        flag=1
        break
    elif a>k:
        print("太大了，请重新输入")
        continue
    else :
        print("太小了，请重新输入")
        continue
if not flag:
    print('次数用完了，游戏结束')
