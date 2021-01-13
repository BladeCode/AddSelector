# -*- encoding: utf-8 -*-
# 数据来源：国家统计局


import requests
from bs4 import BeautifulSoup

# 网站地址
url_2009 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2009/index.html'
url_2010 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2010/index.html'
url_2011 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2011/index.html'
url_2012 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2012/index.html'
url_2013 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/index.html'
url_2014 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/index.html'
url_2015 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/index.html'
url_2016 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html'
url_2017 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html'
url_2018 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html'
url_2019 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "max-age=0",
    "Host": "www.stats.gov.cn",
    "Dnt": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
}

html_content = requests.get(url_2009, headers=headers)
# 声明bs对象和解析器
soup = BeautifulSoup(html_content.content, 'lxml', from_encoding='utf-8')
# 格式化代码，自动补全代码，进行容错的处理
# print(soup.prettify())
# 打印出title标签中的内容
# print(soup.title.string)

for address in soup.select('.provincetr td'):
    if address.a is not None:
        print('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2009/' + address.a.attrs['href'])
        print(address.a.text)
    else:
        print(address.text)
# 组装数据格式
