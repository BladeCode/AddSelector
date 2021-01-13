# -*- encoding: utf-8 -*-
# 数据来源：中华人民共和国民政部

import requests
from bs4 import BeautifulSoup

# 网站地址
url_1980 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708040959.html'
url_1981 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041004.html'
url_1982 = 'http://www.mca.gov.cn/article/sj/xzqh/1980/1980/201911180942.htm'
url_1983 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708160821.html'
url_1984 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220856.html'
url_1985 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220858.html'
url_1986 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220859.html'
url_1987 = 'http://www.mca.gov.cn/article/sj/xzqh/1980/1980/201911180950.htm'
url_1988 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220903.html'
url_1989 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041017.html'
url_1990 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041018.html'
url_1991 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041020.html'
url_1992 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220910.html'
url_1993 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041023.html'
url_1994 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220911.html'
url_1995 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220913.html'
url_1996 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220914.html'
url_1997 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220916.html'
url_1998 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220918.html'
url_1999 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220921.html'
url_2000 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220923.html'
url_2001 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220925.html'
url_2002 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220927.html'
url_2003 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220928.html'
url_2004 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220930.html'
url_2005 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220935.html'
url_2006 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220936.html'
url_2007 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220939.html'
url_2008 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220941.html'
url_2009 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220943.html'
url_2010 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220946.html'

# 县以上行政区划代码
url_2011 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201707271552.html'
# 县以上行政区划代码
url_2012 = 'http://www.mca.gov.cn/article/sj/tjbz/a/201713/201707271556.html'
# 县以下行政区划代码
url_2012_county_after = 'http://files2.mca.gov.cn/cws/201307/20130711193420826.htm'
# 县以上行政区划代码
url_2013 = 'http://files2.mca.gov.cn/cws/201404/20140404125552372.htm'
# 县以下行政区划代码
url_2013_county_after = 'http://files2.mca.gov.cn/cws/201404/20140404125738290.htm'

# 县以上行政区划代码
url_2014 = 'http://files2.mca.gov.cn/cws/201502/20150225163817214.html'
# 县以下行政区划变更情况【格式比较特别，是表格】
url_2014_change_record = 'http://www.mca.gov.cn/article/sj/tjbz/a/2014/201706020952.html'
# 县以上行政区划代码
url_2015 = 'http://www.mca.gov.cn/article/sj/tjbz/a/2015/201706011127.html'
# 县以下行政区划变更情况【格式比较特别，是表格】
url_2015_change_record = 'http://www.mca.gov.cn/article/sj/tjbz/a/2015/below/201602/20160200880232.htm'
# 县以上行政区划代码
url_2016 = 'http://www.mca.gov.cn/article/sj/xzqh/1980/201705/201705311652.html'
# 县以下行政区划变更情况【格式比较特别，是表格】
url_2016_change_record = 'http://www.mca.gov.cn/article/sj/xzqh/1980/201705/201705051130.html'
# 县以上行政区划代码
url_2017 = 'http://www.mca.gov.cn/article/sj/xzqh/1980/201803/201803131454.html'
# 县以下行政区划变更情况【格式比较特别，是表格】
url_2017_change_record = 'http://www.mca.gov.cn/article/sj/xzqh/1980/201803/201803131629.html'
# 县以上行政区划代码
url_2018 = 'http://www.mca.gov.cn/article/sj/xzqh/1980/201903/201903011447.html'
# 县以下行政区划变更情况【格式比较特别，是表格】
url_2018_change_record = 'http://www.mca.gov.cn/article/sj/xzqh/2018/201903/201903011016.html'
# 县以上行政区划代码
url_2019 = 'http://www.mca.gov.cn/article/sj/xzqh/1980/2019/202002281436.html'
# 县以下行政区划变更情况【格式比较特别，是表格】
url_2019_change_record = 'http://www.mca.gov.cn/article/sj/xzqh/1980/2019/202004161449.html'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "max-age=0",
    # "Host": "www.mca.gov.cn",
    "Dnt": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
}

html_content = requests.get(url_2013_county_after, headers=headers)

# 声明bs对象和解析器
soup = BeautifulSoup(html_content.content, 'lxml', from_encoding='utf-8')

for address in soup.select('td'):
    if address.text != '':
        # 空内容不计入并去除两边空格
        print(address.text.strip())
# 组装数据格式
