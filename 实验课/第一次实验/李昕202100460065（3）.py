def AjiaoB(b,c):  #交集
    k=set()
    for i in b:
        if i in c:
          k.add(i)
    return k

def AbingB(b,c):  #并集 
    k=set()
    for i in b:
        if i not in k:
            k.add(i)
    for i in c:
        if i not in k:
            k.add(i)
    return k

def AjianB(b,c):  #差集
    k=set()
    for i in b:
        if i not in c:
            k.add(i)
    return k

b={1,2,3,5,6,8,9}
c={2,3,4,6,7,9,10,15}
print(AjiaoB(b,c))
print(AbingB(b,c))
print(AjianB(b,c))
print(b & c) #交集
print(b | c) #并集
print(b.difference(c)) #差集
