# reference: https://jecvay.com/2014/09/python3-web-bug-series2.html
# python 3.4
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib.request
import urllib

from collections import deque

queue = deque()
visited = set()

url = 'http://news.dbanotes.net'

queue.append(url)
cnt = 0
while queue:
    url = queue.popleft()
    visited |= {url}

    print('already catch：' + str(cnt) + ' catching <----- ' + url)
    cnt += 1
    urlop = urllib.request.urlopen(url, timeout=2)
    if 'html' not in urlop.getheader('Content-Type'):
        continue

    try:
        data = urlop.read().decode('utf-8')
    except:
        continue

linkre = re.compile(('href="(.+?)"'))
for x in linkre.findall(data):
    if 'http' in x and x not in visited:
        queue.append(x)
        print('add to queue--->' + x)
