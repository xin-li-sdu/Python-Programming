#UDP适用于对效率要求高而对准确性要求相对较低的场合
import socket
import sys
import time
 
HOST="127.0.0.1"
PORT=50007

while True:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#SOCK_DGRAM表示UDP协议
    s.sendto('ask for time'.encode(),(HOST,PORT))
    data,addr=s.recvfrom(1024)#接收数据，接收小于 1024 字节的数据
    print(data.decode())
    s.close()
    time.sleep(1)
