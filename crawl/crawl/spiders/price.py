from scrapy.spider import Spider 
from crawl.items import HKpriceItem

def count_url(n):
    initurl = 'https://www.price.com.hk/search.php?g=A&q=gtx+1080'
    urls = []
    for i in range(n):
        url = initurl + '&page=' + str(i+1) 
        urls.append(url)
    return urls

class Pricehk(Spider):
    name = 'gtx1080'
    start_urls = count_url(7)

    def parse(self, response):
        products = response.xpath('//div[@class="list-product"]/ul/li')
        for product in products:
            item = HKpriceItem()
            item['product'] = product.xpath('.//div[@class="line line-01"]//a/text()').extract()
            item['desc'] = product.xpath('.//div[@class="line line-02"]/span/text()').extract()
            item['price'] = product.xpath('.//div[@class="listing-price-range"]/span[2]/text()').extract()
            item['priceh'] = product.xpath('.//div[@class="listing-price-range"]/span[4]/text()').extract()
            yield item
