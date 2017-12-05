from scrapy.spider import Spider 

class WikiSpider(Spider):
    name = 'wiki'
    #allowed_domains = ['wikipedia.org']
    start_urls = [
        u'http://woodenrobot.me',
    ]

    def parse(self, response):
        titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            print title.strip()