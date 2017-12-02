# -*- coding: utf-8 -*-

import string, urllib2

def tieba(url, begin, last):
    for i in range(begin, last):
        filename = string.zfill(i, 3)+'.html'
        f = open(filename, 'w+')
        content = urllib2.urlopen(url+str(i * 50)+'.html').read()
        f.write(content)
        f.close()
        print 'successfully saved page: ' + str(i) + 'to' + filename

url = str(raw_input('please type in chiphell forum location, do not type last number!:\n'))
begin = int(raw_input('which page do you want to begin:\n'))
last = int(raw_input('which page do you want to stop:\n'))

tieba(url, begin, last)