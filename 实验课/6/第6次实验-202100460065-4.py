import socket
import re
def scan(ip): 
    begin,end = (134,140) #输入范围范围值
    for i in range(int(begin),int(end)+1):  
        s = socket.socket()
        conn = s.connect_ex((ip,i)) #该方法如果链接成功会返回0
        if conn ==0:
            print("主机:",ip,"端口:",i,"开放！！！！")
        else:
           print("主机:",ip,"端口:",i,"未开放")
        s.close()    
ip = input('请输入要扫描的ip：')
ip1= re.compile('((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
if(ip1.match(ip)): #判断格式是否正确
    scan(ip)
else:
  print("格式错误！")

