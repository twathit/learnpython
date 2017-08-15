# -*- coding: utf-8 -*-
__author__ = 'Edward'
from html.parser import HTMLParser
import chardet
class MyHtmlParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.time=None
        self.span=None
        self.mark=[]
        self.datetime=[]
        self.year=[]
        self.location=[]
        self.title=[]
        self.say=None
        self.h3=None
    def handle_starttag(self, tag, attrs):
        if tag=='time':
            self.time=True

        if tag=='span':
            self.time=False
            for c,d in attrs:
                if d=='event-location':
                    self.span=True
                if d=='say-no-more':
                    self.say=True
        if tag=='h3':
            for c,d in attrs:
                if d=='event-title':
                   self.h3=True
    def handle_endtag(self, tag):
        if tag=='span':
            self.span=False
            self.say=False
        if tag=='time':
            self.time=False
        if tag=='h3':
            self.h3=False
    def handle_data(self, data):
        if self.span:
            self.location.append(data)
        if self.time:
            self.datetime.append(data)
        if self.say:
            self.year.append(data)
        if self.h3:
            self.title.append(data)

parser=MyHtmlParser()
with open(r'e:/python/pyevent.html','r') as f:
    html=str(f.read())
parser.feed(html)
for i in range(len(parser.location)):
    print('会议名称:',parser.title[i])
    print('会议时间:',parser.datetime[i],parser.year[i])
    print('会议地点:',parser.location[i])

