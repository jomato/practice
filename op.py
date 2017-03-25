#-*- encoding:utf8 -*-
from lxml import html, etree
import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import re
import json
import urllib2

cont = '''<?xml version="1.0" encoding="ISO-8859-1"?>

<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
  <title lang="en">Harry Potter</title>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>'''

# text = etree.HTML(cont)
# print text
# print text.xpath('.')
'''print text.xpath('book/title/node()')#选取title节点下的所有类型的节点
print text.xpath("//book[price/node()>30]")#选取所有book元素，其中的子元素price的值大于30也可以写成'//book[price>30]

content = html.fromstring(cont)
print content.xpath('//title[@lang = "en"]')
print content.xpath('*/node()')#选取当前节点下的子元素下的节点（！！！！！切记必须是在当前节点下的子元素下）('\n',是文本节点)
print content.xpath('book/title[last()-1]')#选取book元素下的倒数第二个title子元素
print content.xpath('//bookstore/book/title[last()]/@*')#选取book元素下的倒数第一个title子元素的属性节点的值
print content.xpath('..')[0].xpath('..')#返回父节点的父节点
####以'//'开头表示他们在文档中的位置，以'/'开头表示绝对路径，不以任何斜杠开头表示在当前节点下选取'''



'''headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2593.0 Safari/537.36',
                   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'cache-control':'max-age=0',
                   'upgrade-insecure-requests':'1',
                   'accept-encoding':'gzip, deflate, sdch'}
url = 'https://mm.taobao.com/self/aiShow.htm?userId=176817195'
req = requests.get(url,headers=headers)
content = req.content
co = req.text
soup = BeautifulSoup(co, 'lxml')
tags = soup.find_all('img', {"src": re.compile(r".*\.jpg")})
for tag in tags:
    print 'http:'+tag['src']'''

'''print type(co)
print type(content)
print co'''
'''print html.fromstring(content)
text = html.fromstring(content)
cext = html.fromstring(co)
print cext.xpath('//body')
print text.xpath('//div[@class="girls-list-wrap"]/ul')
#soup = BeautifulSoup()'''



'''isexists = os.path.exists(r'E:\jian'+'/'+'中文')
st = '中文'.decode('utf8').encode('gbk')
if not isexists:
    os.makedirs(r'E:\jian'+'/'+st)
    print '创建完毕'
else:
    print "已存在"'''



'''driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8')
htm = driver.page_source
print htm'''



'''headers = {'accept':'application/json, text/javascript, */*; q=0.01',
           'accept-encoding':'gzip, deflate',
           'accept-language':'zh-CN,zh;q=0.8',
           'content-length':'106',
           'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
           'cookie':'cna=2/oNEKKOaxICAZ090jcVr73q; miid=8734663056256283667; thw=cn; CNZZDATA30063598=cnzz_eid%3D1243648137-1470467097-%26ntime%3D1470589024; v=0; cookie2=1f5e04d47c280ca2dd3a71e94cd75413; t=7b54ddc9aeefd9fc625117b5b6bd0433; _tb_token_=e6136ef769e39; mt=ci%3D-1_0; JSESSIONID=591E4C0FDA80CC47831E19306588083F; uc1=cookie14=UoWwJM9KLm%2FOzg%3D%3D; l=Aq2tf23qVX7tihXGwteOXAX6PUMgluEj; isg=AsDAubylgyvQ8X8UlmAoceOkkU6GDS82ZgtlojpWEFuRtWTf4lgsokLDu6qO',
           'origin':'https://mm.taobao.com',
           'referer':'https://mm.taobao.com/search_tstar_model.htm?',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2593.0 Safari/537.36',
           'x-requested-with':'XMLHttpRequest'}

j_headers = json.dumps(headers)'''

'''req = requests.get('https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8')
print req.text'''

'''url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'

req = urllib2.Request(url, headers=headers)
content = urllib2.urlopen(req).read()
print content'''


'''path, dirs, df, names = os.walk(r'E:/jian')
print os.walk(r'E:/jian')
print path
print dirs
print df
print names'''
'''for path, dir, names in os.walk(r'E:/jian'):
 print path
    print dir
    print names
    for name in names:
        print name'''


# isexits = os.path.exists('E:taobao\\test')
# if not isexits:
#     print isexits
#     os.makedirs('E:taobao\\test')




bool_ = False
if bool_:
    print 'True'
else:
    print 'Flase'


# a = 123
# a = str(a)
# b = a.split()
# lst = list(a)
# print b
# print list
# lst.reverse()
# c = ''.join(lst)
# c = int(c)
# print repr(lst)
# print type(c)
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    xstr = str(x)
    xlst = list(xstr)
    xlst.reverse()
    x = ''.join(xlst)
    x = int(x)
    return x


def insert_sort(lists):
    # 这是插入排序
    for i in xrange(1, len(lists)):
        k = i-1
        key = lists[i]
        while k >= 0:
            if lists[k] > key:
                lists[k+1], lists[k] = lists[k], key
            k -= 1
    return lists

ls = [9, 8, 7, 6, 5, 4, 3, 2, 10]
# print insert_sort(ls)


def select_sort(lists):
    # 这是选择排序
    for i in xrange(0, len(lists)):
        for j in xrange(i+1, len(lists)):
            if lists[j] < lists[i]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


# print select_sort(ls)




