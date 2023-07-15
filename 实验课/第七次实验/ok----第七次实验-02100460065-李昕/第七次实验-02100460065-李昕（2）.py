import urllib.request
import re

#获得目标网页全部源代码    
def getHtml(url):
    #目标头部信息
    headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }   
    #url作为Request()方法的参数，构造并返回一个符合headers要求的Request对象
    req = urllib.request.Request(url, headers=headers)
    #Request对象作为urlopen()方法的参数，发送给服务器并接收响应
    fp = urllib.request.urlopen(req)
    #读取指定网页全部源代码并解码
    htmlCode = fp.read().decode()
    #返回文本
    return htmlCode
 
#获得下载地址并进行下载    
def getImg(htmlCode):
    #构建正则表达式对象
    reg = r'src="(.+?\.jpg)" pic_ext'   
    imgre = re.compile(reg)
    imglist = imgre.findall(htmlCode) #如果正则表达式带子模式，findall返回括号中匹配的
    #计数变量，用于命名
    x=0
    #图片存放的目录，默认空串为当前目录
    paths = ""    
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'{}{}.jpg'.format(paths,x))  
        x = x + 1
htmlCode = getHtml("http://tieba.baidu.com/p/2460150866")
getImg(htmlCode) 
print("OVER")
