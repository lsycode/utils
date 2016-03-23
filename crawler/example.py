# python 3.4
# reference :http://www.yiibai.com/python/python3-webbug-series1.html
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import http.client
import urllib.request

url = "http://www.baidu.com"

res = urllib.request.urlopen(url)

print(type(res))

data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')


