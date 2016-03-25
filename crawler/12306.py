# python 3.4
# reference :http://www.yiibai.com/python/python3-webbug-series1.html
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import time
import webbrowser

url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2016-04-04&leftTicketDTO.from_station=JYK&leftTicketDTO.to_station=BJP&purpose_codes=ADULT"

format = "%H:%M"
start_time1 = "16:00"
start_time2 = "22:00"
start_time1 = time.strptime(start_time1, format)
start_time2 = time.strptime(start_time2, format)
res = urllib.request.urlopen(url)

while True:
    resp = urllib.request.urlopen(url).read()
    resp = resp.decode('UTF-8')
    data = json.loads(resp)["data"]
    array = []
    for x in data:
        jdata = x["queryLeftNewDTO"]
        t = str(jdata["start_time"])
        t = time.strptime(t, format)
        if t < start_time1 or t > start_time2:
            continue
        s = {"车次": jdata["station_train_code"], "开始时间": jdata["start_time"], "软卧": jdata["rw_num"],
             "硬卧": jdata["yw_num"]}
        array.append(s)
    print(array)
    rw = s.get("软卧")
    yw = s.get("硬卧")
    if (rw != "无" or yw != "无"):
        webbrowser.open()
        break
    time.sleep(2)

with open(r'C:\Users\andy\Desktop\12306.txt', 'w', encoding='utf-8') as f:
    f.write(str(data))
