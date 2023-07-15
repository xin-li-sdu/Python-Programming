def perfect(a): #输出1000以内的完数
    b=[]
    for i in range(1,a):
        if a%i==0:
            b.append(i)
    c=lambda b:sum(b)
    if c(b)==a:
        return True
    else:
        return False
print('1000以内的完数：',list(filter(perfect,range(1,1000))))
