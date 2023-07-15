import requests
from bs4 import BeautifulSoup
import os
# 本地写入
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
def getPage(url):
    re=requests.get(url,headers=headers)
    re.raise_for_status()
    re.encoding=re.apparent_encoding
    soup=BeautifulSoup(re.text,'lxml')
    return soup
if __name__ == '__main__':
    url='https://www.biqukan8.cc/2_2671'
    soup=getPage(url)
    book_name=soup.select('.info h2')[0].text
    book_author=soup.select('.small span')[0].text
    last_time=soup.select('.small .last')[0].text
    last_chapter=soup.select('.small .last a')[0].text
    print("书名:",book_name,book_author,last_time,"最新章节:",last_chapter)
    # 以书名创建文件夹
    k=os.path.exists(book_name) # k为bool类型
    if k==False:
        # 没有才创建
        os.makedirs(book_name)
    # 获取所有单章链接
    links=soup.select('.listmain dd a')
    # 前12个为最新章节，其余为正式章节，包含最新章节
    for item in links[12:]:
        href='https://www.biqukan8.cc/'+item['href']
        print(href,item.string)
        soup=getPage(href)
        content=soup.select('.showtxt')[0].text
        content=content.replace('app2();read2();　　','')
        content=content.replace('　　','\n\n')
        print(">>>正在写入文件")
        with open("%s/%s.txt"%(book_name,item.string),'w',encoding='utf-8') as file:
            file.write(content)
    print(">>>全部章节爬取完毕！")

