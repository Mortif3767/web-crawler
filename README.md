# 几个简单web爬虫  
  
### crawl  
基于scrapy，主要功能：对香港报价网www.price.com.hk中所有GTX1080显卡汇总，爬取商品名称、简介、最低报价、最高报价。  
spider位置：`crawl/price.py`。  
  
### baidutieba.py  
基于urllib2的轻量爬虫，可爬取百度贴吧帖子，只看楼主所有楼层，并合并导出到txt。  
  
### qiubai.py  
基于urllib2的轻量爬虫，可爬取最新的糗事百科主页条目，按回车键刷新下一页。  
  
### chiphell.py  
初步练手，可以下载贴吧指定页面html。
