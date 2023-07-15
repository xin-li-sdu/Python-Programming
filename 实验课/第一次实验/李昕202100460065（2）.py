def sum(a):  #求任意大自然数的每位的和
    b=0
    while(a/10>0):
        b=b+a % 10
        a=a//10
    return b
a=input("请输入一个任意大的自然数:")
a=int(a)
print(sum(a))
