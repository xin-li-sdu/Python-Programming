import socket
import sys
HOST='127.0.0.1' #服务器IP地址和端口号
PORT=1234
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((HOST,PORT)) #连接服务器
except Exception as e: #捕捉异常
    print('not found or not open, please try again!')
    sys.exit()
while True:
    c=input('Please input the content you want to send:')
    s.sendall(c.encode())#发送数据同时使用UTF-8编码
    data=s.recv(1024)#接收数据，接收小于 1024 字节的数据
    data=data.decode()
    print('Received：',data)
    if c.lower()=='bye':
        break
s.close()#关闭连接

    
