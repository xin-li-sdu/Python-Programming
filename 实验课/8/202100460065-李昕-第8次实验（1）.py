from bs4 import BeautifulSoup
import requests
import re
import sys

nums = 0
names = []
urls = []

headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}   #头部信息

def get_download_url(server,target,names,urls):
    '''
    获取要爬取的链接
    '''
    req = requests.get(url = target,headers = headers, verify =  False )
    html = req.text
    li_bf = BeautifulSoup(html,features="html.parser")
    li = li_bf.find_all('li', class_ = 'name_list')
    #print(li)
    global nums
    nums = len(li)
    for each in li:
        a_bf = BeautifulSoup(str(each),features="html.parser")
        a = a_bf.find_all('a') #每个院士姓名下就一个<a href...
        names.append(a[0].string) #获取链接的名字
        tstr = server + a[0].get('href') #获取"href"属性的值，即链接
        urls.append(tstr)
        


def get_contents(target):
    '''函数说明:获取院士信息'''
    req = requests.get(url=target, headers = headers, )
    req.encoding = 'utf-8'
    #print(req.encoding)
    html = req.text
    bf = BeautifulSoup(html,features="html.parser")
    div = bf.find_all('div', class_ = 'intro')
    #print(div)
    txt = ''
    p_bf = BeautifulSoup(str(div[0]),features="html.parser")
    p = p_bf.find_all('p') #若干<p>…</p>
    for each in p:
        txt += each.text
    #print(txt) 
    return txt

def writer(name, filename, text):
    write_flag = True
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(name + '\n')
        f.writelines(text)
        f.write('\n\n')

 
if __name__ == '__main__':
    pat = r"\xa0+"
    server = 'http://www.cae.cn'
    target = 'http://www.cae.cn/cae/html/main/col48/column_48_1.html'
    nmus = 0
    get_download_url(server,target,names,urls)
    print('工程院院士信息开始下载：')
    print('nums = ',nums)
    
