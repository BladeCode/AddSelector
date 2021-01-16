# AddSelector

```
AddSelector/
    ├── code/           # python 爬虫脚本
    │   ├── MCA/        # 中华人民共和国民政部
    │   └── NBS/        # 国家统计局
    ├── data/           # 对应年份的 json 数据文件
    ├── .gitignore
    ├── LICENSE
    └── README.md
```

本项目仅为学习Python 的实践项目，切勿商业用途，由于是政府网站，大家都懂，请合理的进行爬取数据

使用框架
* BeautifulSoup

## 数据说明

>[用区划代码和城乡划分代码编制规则](http://www.stats.gov.cn/tjsj/tjbz/200911/t20091125_8667.html)

## 数据来源

* National Bureau of Statistics [国家统计局 - 用区划和城乡划分代码](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm)
* Ministry of Civil Affairs, PRC [中华人民共和国民政部 - 用区划和城乡划分代码](http://www.mca.gov.cn/article/sj/xzqh/)

### 数据历史

#### 国家统计局

* ~~[统计截至时间：2009.01.01 发布时间：2013.11.16](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2009/index.html)~~
* ~~[统计截至时间：2010.01.01 发布时间：2013.11.16](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2010/index.html)~~
* ~~[统计截至时间：2011.01.01 发布时间：2013-11-06](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2011/index.html)~~
* ~~[统计截至时间：2012-10-31 发布时间：2013-11-06](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2012/index.html)~~
* ~~[统计截至时间：2013-08-31 发布时间：2014-01-16](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/index.html)~~
* ~~[统计截至时间：2014-10-31 发布时间：2016-01-19](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/index.html)~~
* ~~[统计截至时间：2015-09-30 发布时间：2016-07-27](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/index.html)~~
* ~~[统计截至时间：2016-07-31 发布时间：2017-05-16](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html)~~
* ~~[统计截至时间：2017-10-31 发布时间：2018-06-20](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html)~~
* ~~[统计截至时间：2018-10-31 发布时间：2019-01-31](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html)~~
* ~~[统计截至时间：2019-10-31 发布时间：2020-02-25](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html)~~
* [最新统计截至时间：2020-06-30 发布时间：2020-11-06](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/index.html)

#### 民政部

>[中华人民共和国乡镇行政区划简册勘误-2016](http://www.mca.gov.cn/article/sj/xzqh/jckw/)
* ~~[1980年中华人民共和国行政区划代码（截止1980年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708040959.html)~~
* ~~[1981年中华人民共和国行政区划代码（截止1981年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041004.html)~~
* ~~[1982年中华人民共和国行政区划代码（截止1982年12月31日）](http://www.mca.gov.cn/article/sj/xzqh/1980/1980/201911180942.html)~~
* ~~[1983年中华人民共和国行政区划代码（截止1983年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708160821.html)~~
* ~~[1984年中华人民共和国行政区划代码（截止1984年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220856.html)~~
* ~~[1985年中华人民共和国行政区划代码（截止1985年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220858.html)~~
* ~~[1986年中华人民共和国行政区划代码（截止1986年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220859.html)~~
* ~~[1987年中华人民共和国行政区划代码（截止1987年12月31日）](http://www.mca.gov.cn/article/sj/xzqh/1980/1980/201911180950.html)~~
* ~~[1988年中华人民共和国行政区划代码（截止1988年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220903.html)~~
* ~~[1989年中华人民共和国行政区划代码（截止1989年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041017.html)~~
* ~~[1990年中华人民共和国行政区划代码（截止1990年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041018.html)~~
* ~~[1991年中华人民共和国行政区划代码（截止1991年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041020.html)~~
* ~~[1992年中华人民共和国行政区划代码（截止1992年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220910.html)~~
* ~~[1993年中华人民共和国行政区划代码（截止1993年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708041023.html)~~
* ~~[1994年中华人民共和国行政区划代码（截止1994年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220911.html)~~
* ~~[1995年中华人民共和国行政区划代码（截止1995年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220913.html)~~
* ~~[1996年中华人民共和国行政区划代码（截止1996年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220914.html)~~
* ~~[1997年中华人民共和国行政区划代码（截止1997年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220916.html)~~
* ~~[1998年中华人民共和国行政区划代码（截止1998年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220918.html)~~
* ~~[1999年中华人民共和国行政区划代码（截止1999年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220921.html)~~
* ~~[2000年中华人民共和国行政区划代码（截止2000年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220923.html)~~
* ~~[2001年中华人民共和国行政区划代码（截止2001年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220925.html)~~
* ~~[2002年中华人民共和国行政区划代码（截止2002年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220927.html)~~
* ~~[2003年中华人民共和国行政区划代码（截止2003年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220928.html)~~
* ~~[2004年中华人民共和国行政区划代码（截止2004年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220930.html)~~
* ~~[2005年中华人民共和国行政区划代码（截止2005年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220935.html)~~
* ~~[2006年中华人民共和国行政区划代码（截止2006年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220936.html)~~
* ~~[2007年中华人民共和国行政区划代码（截止2007年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220939.html)~~
* ~~[2008年中华人民共和国行政区划代码（截止2008年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220941.html)~~
* ~~[2009年中华人民共和国行政区划代码（截止2009年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220943.html)~~
* ~~[2010年中华人民共和国行政区划代码（截止2010年12月31日）](http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708220946.html)~~
* ~~[2011年中华人民共和国行政区划代码（截止2011年12月31日）](http://www.mca.gov.cn/article/sj/xzqh/1980/201706/20170615004707.shtml)~~
* ~~[2012年中华人民共和国行政区划代码（截止2012年12月31日）](http://www.mca.gov.cn/article/sj/xzqh/1980/201507/20150715854921.shtml)~~
* ~~[2013年中华人民共和国行政区划代码（截止2013年12月31日）](http://www.mca.gov.cn/article/sj/xzqh/1980/201507/20150715854922.shtml)~~
* ~~[2014年中华人民共和国行政区划代码（截止2014年12月31日）](http://www.mca.gov.cn/article/sj/xzqh/1980/201507/20150715854923.shtml)~~
* ~~[2015年中华人民共和国行政区划代码（截止2015年12月31日）](http://www.mca.gov.cn/article/sj/xzqh/1980/201611/20161115002410.shtml)~~
* ~~[2016年中华人民共和国行政区划代码（截止2016年12月31日）](http://www.mca.gov.cn/article/sj/xzqh/1980/201705/20170515004409.shtml)~~
* ~~[2017年中华人民共和国行政区划代码（截止2017年12月31日）](http://www.mca.gov.cn/article/sj/xzqh/1980/201803/20180315008048.shtml)~~
* ~~[2018年中华人民共和国行政区划代码（截止2018年12月31日）](http://www.mca.gov.cn/article/sj/xzqh/1980/201903/20190300014989.shtml)~~
* ~~[2019年中华人民共和国行政区划代码（截止2019年12月31日）](http://www.mca.gov.cn/article/sj/xzqh/1980/202002/20200200025008.shtml)~~
* [2020年中华人民共和国行政区划代码](http://www.mca.gov.cn/article/sj/xzqh/2020/)
