def jinzhi(d):  #输出二进制、八进制和十六进制表示
    print(bin(d))
    print(oct(d))
    print(hex(d))

d=int(input("请输入一个自然数："))
jinzhi(d)
print("{0:b}".format(int(d))) #二进制
print("%o" % d) #八进制
print("%x" % d) #十六进制
