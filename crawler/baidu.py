# python 3.4
# reference :http://www.yiibai.com/python/python3-webbug-series1.html
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import http.client
import urllib.request
import urllib.parse

url = "http://www.baidu.com"

res = urllib.request.urlopen(url)

data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')

data = {}
data['word'] = 'jack'
url_values = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + url_values
data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
with open(r'C:\Users\andy\Desktop\crawler.html', 'w', encoding='utf-8') as f:
    f.write(data)
