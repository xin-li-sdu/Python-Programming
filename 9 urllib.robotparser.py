import urllib.request
import urllib.parse

import urllib.robotparser

'''
parse()：用来解析robots.txt文件，
         传入的参数是robots.txt的某些行的内容，
         它会按照robots.txt的语法规则分析这些内容。

can_fetch()：传入两个参数，User-agent和要抓取的URL，
            它将会判断该搜索引擎能否抓取这个URL，返回False或True。
             *代表该协议是否对任何爬虫都有效。
'''

rp = urllib.robotparser.RobotFileParser()
rp.parse(urllib.request.urlopen('http://www.python.org/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch("*", "http://www.python.org/downloads/"))
print(rp.can_fetch("*", "http://www.python.org/webstats/"))
