# -*- coding: utf-8 -*-
"""
Created on 2022-11-19 22:38:13
---------
@summary:
---------
@author: waldeinsamkeit
"""

import feapder
import re
 
#写入文件函数，规定写入的格式
def writer(filename, text):
    with open(filename, 'a', encoding='utf-8') as f:
        f.writelines(text)
        f.write('\n\n')
 
#轻量级爬虫 AirSpider
class yuanshi(feapder.AirSpider):
    def start_requests(self):
        url='https://www.cae.cn/cae/html/main/col48/column_48_1.html'
        yield feapder.Request(url)
    
    #爬取院士名单和对应的链接地址
    def parse_name(self, response):
        #利用xpath过滤得到目标标签
        name_list=response.xpath("//*[@class='name_list']")
        for name in name_list:
            #extract_first()：这个方法返回的是一个string字符串，是list数组里面的第一个字符串
            #得到对应院士的链接
            href=name.xpath('.//@href').extract_first()
            yield feapder.Request(href,callback=self.parse_next)
    
    #爬取院士信息
    def parse_content(self,request,response):
        #利用xpath过滤得到目标标签
        intro=response.xpath("//*[@class='intro']")
        #extract():这个方法返回的是一个数组list
        #注意这里的解析是Unicode编码
        t=intro.xpath(".//p[contains(text(),'\u2002')]").extract()
        #转成字符串进行后续处理
        tt=''.join(t)
        regp = r'<p>([\s\S]+?)</p>'
        intropre = re.compile(regp)
        introlist=re.findall(intropre,tt)
        ttt=''
        for cont in introlist:
            ttt+=str(cont)
        #写入
        writer('院士.txt', ttt)
        #print(ttt)
 
if __name__ == "__main__":
    yuanshi().start()
