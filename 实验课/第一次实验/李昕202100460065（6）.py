def list1():  #构造一个元素为1000以内的所有素数的列表
    k=list()
    for i in range(0,1000):
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            k.append(i)
    return k
print(list1())
