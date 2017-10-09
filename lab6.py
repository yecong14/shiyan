n [1]: import feedparser

In [2]: ny = feedparser.parse('http://labfile.oss.aliyuncs.com/courses/499/ny.txt')

In [3]: sf = feedparser.parse('http://labfile.oss.aliyuncs.com/courses/499/sf.txt')

In [4]: import re

In [5]: data = sf['entries'][11]['summary']

In [6]: regex = re.compile('\\W*')

In [7]: wordlist = regex.split(data)

In [8]: wordlist = [i.lower() for i in wordlist if len(i)>2]

In [9]: from lab5 import *

