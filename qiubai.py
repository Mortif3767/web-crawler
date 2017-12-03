import urllib2, urllib, re, thread, time, json

class Spider:

    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

    def getpage(self, page):
        url = "https://www.qiushibaike.com/hot/page/" + page
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        headers = {'User-Agent': user_agent}
        req = urllib2.Request(url, headers=headers)
        res = urllib2.urlopen(req)
        page = res.read()
        unicodepage = page.decode('utf-8')
        items = re.findall('<div.*?class="content">.*?<span>(?P<content>.*?)</span>.*?</div>',
                           unicodepage, re.DOTALL)
        return items

    def showpage(self, items):
        for i in range(0,len(items)):
            print items[i].replace('<br/>', "")

    def start(self):
        self.enable = True
        page = self.page
        try:
            items = self.getpage(str(page))
            self.showpage(items)
            self.page = page + 1
        except:
            print 'cannot connect!'

print 'press anykey to begin'
spider = Spider()
while raw_input('') is not None:
    spider.start()