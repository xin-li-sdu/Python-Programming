a=[0]*52 #分别存储小写和大写的个数
try :
    k=open(r"C:\Users\lenovo\Documents\1.txt",mode='r',encoding = 'utf-8')
except FileNotFoundError:
    print("没有这个文件")
else :
    m=k.readlines()
    for i in m:
        for j in i:
            if j.isupper():
                a[ord(j)-39]=a[ord(j)-39]+1
            elif j.islower():
                a[ord(j)-97]=a[ord(j)-97]+1
    for i in range(26):
        print(chr(i+97),'有',a[i],'个',end='\n')
    for i in range(26,52):
        print(chr(i+39),'有',a[i],'个',end='\n ')
    k.close()
