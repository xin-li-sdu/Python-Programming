import socketserver
from os.path import commonprefix
from os.path import commonprefix
words={"what's your name?":'lixin',
      'what time is it?':'It is 8:00 am', 
      'how old are you?':'20 years old hahaha',
      'where do you work?':'SDU!!',
      'how are you?':'Fine,thank you!',
      'bye':'Bye!'}#创建智能识别的问题库


class MyTCPhanler(socketserver.BaseRequestHandler):
  def handle(self):
    while True:
      try:
        data = self.request.recv(1024).decode()
        print('Received message:',data)
        #尽量猜测对方要表达的意思
        m=0
        key=''
        for k in words.keys():
            data=' '.join(data.split()) #删除多余的空白字符
            #与某个键非常接近，就直接返回
            if len(commonprefix([k,data]))>len(k)*0.7:
                key=k;break
            length=len(set(data.split())&set(k.split()))
            if length>m:
                m=length;key=k
        self.request.send(words.get(key,'Sorry.').encode())
      except ConnectionResetError:
        break
    self.request.close()
if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',1234),MyTCPhanler)
    server.serve_forever()# 链接循
