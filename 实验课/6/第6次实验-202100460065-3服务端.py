# 服务端必须满足至少三点
#1. 绑定一个固定的ip和port
#2. 一直对外提供服务,稳定运行
#3. 能够支持并发
import socketserver


class MyTCPhanler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                data = self.request.recv(1024)
                if len(data) == 0:
                    break
                print('-->收到客户端的消息: ', data)
                self.request.send(data.upper())
            except ConnectionResetError:
                break
        self.request.close()
if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',8081),MyTCPhanler)
    server.serve_forever() # 链接循环
