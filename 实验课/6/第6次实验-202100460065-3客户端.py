from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8081))

# 通信循环
while True:
    sdata = input("please enter the data:")
    if sdata == 'q':
        break
    client.send(sdata.encode('utf-8'))#发送数据同时使用UTF-8编码
    data=client.recv(1024)#接收数据，接收小于 1024 字节的数据
    print(data)
client.close()#关闭连接
