import urllib.request
#用urlopen()创建urllib连接对象
fp = urllib.request.urlopen(r'http://www.baidu.com')
#read()可以读取网页超文本源代码，也就是HTML代码
#参数为指定读取内容大小，无参数默认全部文本
#需要解码，否则会直接返回十六进制编码字符串
print(fp.read().decode())
#关闭连接对象
fp.close()
