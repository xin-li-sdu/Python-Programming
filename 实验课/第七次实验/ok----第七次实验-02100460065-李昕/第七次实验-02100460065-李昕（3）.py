import urllib.request
import re

#写入文件函数，规定写入的格式
def writer(name, filename, text):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(name + '\n')
        f.writelines(text)
        f.write('\n\n')
    
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
 
def getContent(html):
    #构建正则对象
    #/s - 匹配任何空白字符，包括空格、制表符、换页符
    #/S - 与\s含义相反
    reg = r'<a href="(.+?\.html)" target="_blank">(.+?)</a>'   
    regintro = r'<div class="intro">([\s\S]+?)</div>'   
    regp = r'<p>([\s\S]+?)</p>'                         
    htmlre = re.compile(reg)
    htmllist = htmlre.findall(html)
    introre = re.compile(regintro)
    intropre = re.compile(regp)
    #计数变量，用于计算下载进度
    for htmlurl,name in htmllist:
        #字符串拼接出院士信息的网址
        htmlcontent = getHtml('http://www.cae.cn'+htmlurl)
        intro_withp = introre.findall(htmlcontent)
        intro_withoutp = intropre.findall(intro_withp[0])
        #信息
        txt = ""
        for cont in intro_withoutp:
            txt += cont.replace('&ensp;','')
        #写入
        writer(name, '工程院士信息.txt', txt)
        allyuanshi = len(htmllist)
htmlCode = getHtml("https://www.cae.cn/cae/html/main/col48/column_48_1.html")     
getContent(htmlCode) 
print("OVER")
