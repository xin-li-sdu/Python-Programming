import socket
from datetime import datetime
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
HOST=""
PORT=50007
s.bind((HOST,PORT))
while True:
    data,addr=s.recvfrom(1024)
    print("received message:{0} from {1}".format(data.decode(),addr[0]))
    now =str(datetime.now())[:19]
    s.sendto(now.encode(),addr)
s.close()
