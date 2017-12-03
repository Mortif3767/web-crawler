import string, urllib2, re

class Tagtool:

    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")  
    EndCharToNoneRex = re.compile("<.*?>")  
    BgnPartRex = re.compile("<p.*?>")  
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")  
    CharToNextTabRex = re.compile("<td>")  
    replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," ")]  
      
    def Replace_Char(self,x):
        x = self.BgnCharToNoneRex.sub("",x)  
        x = self.BgnPartRex.sub("\n",x)  
        x = self.CharToNewLineRex.sub("\n",x)  
        x = self.CharToNextTabRex.sub("\t",x)  
        x = self.EndCharToNoneRex.sub("",x)  
  
        for t in self.replaceTab:    
            x = x.replace(t[0],t[1])
        return x


class Baidutieba:

    def __init__(self, url):
        self.url = url + '?see_lz=1'
        self.datas = []
        self.tool = Tagtool()

    def start(self):
        content = urllib2.urlopen(self.url).read().decode('utf-8')
        pagenum = self.totalpage(content)
        title = self.title(content)
        self.save(self.url, title, pagenum)

    def totalpage(self, content):
        pagenum = re.search('<span.*?class="red">(\d+)</span>', content, re.S)
        if pagenum:
            pagenum = int(pagenum.group(1))
            print 'found total pages: %d' % pagenum
        else:
            pagenum = 0
            print 'unable to found pages!'
        return pagenum

    def title(self, content):
        title = re.search('<title>(.*?)</title>', content, re.S)
        if title:
            title = title.group(1)
            print 'found title: %s' % title
        else:
            title = 'unname'
            print 'title not found!'
        return title

    def save(self, url, title, pagenum):
        self.getdata(url, pagenum)
        f = open(title+'.txt', 'w+')
        f.writelines(self.datas)
        f.close()
        print 'successfully saved!'

    def getdata(self, url, pagenum):
        url = url + '&pn='
        for i in range(1, pagenum+1):
            content = urllib2.urlopen(url+str(i)).read().decode('utf-8')
            self.cleandata(content)

    def cleandata(self, content):
        items = re.findall('id="post_content.*?class="d_post_content.*?">(.*?)</div>',
                           content, re.S)
        for item in items:
            data = self.tool.Replace_Char(item.replace('\n','').encode('utf-8'))
            self.datas.append(data+'\n')


print 'please type in tieba id:'
url = 'http://tieba.baidu.com/p/' + str(raw_input('http://tieba.baidu.com/p/'))

crawl = Baidutieba(url)
crawl.start()