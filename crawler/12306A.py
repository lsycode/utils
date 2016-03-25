# python 3.4
# reference :http://www.yiibai.com/python/python3-webbug-series1.html
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import time
import webbrowser
import threading
import os
from multiprocessing import Pool


def get(td, date, from_station, to_station, start_time, end_time):
    url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=" + date + "&leftTicketDTO.from_station=" + from_station \
          + "&leftTicketDTO.to_station=" + to_station + "&purpose_codes=ADULT"

    format = "%H:%M"
    start_time = time.strptime(start_time, format)
    end_time = time.strptime(end_time, format)

    while True:
        resp = urllib.request.urlopen(url).read()
        resp = resp.decode('UTF-8')
        data = json.loads(resp)["data"]
        array = []
        for x in data:
            jdata = x["queryLeftNewDTO"]
            t = str(jdata["start_time"])
            t = time.strptime(t, format)
            if t < start_time or t > end_time:
                continue
            s = {"车次": jdata["station_train_code"], "日期": date, "软卧": jdata["rw_num"],
                 "硬卧": jdata["yw_num"]}
            array.append(s)
        print("thread " + td + ",")
        print(array)
        rw = s.get("软卧")
        yw = s.get("硬卧")
        if (rw != "无" or yw != "无"):
            webbrowser.open("https://kyfw.12306.cn/otn/login/init")
            break
        time.sleep(30)


lock = threading.Lock()


def run_thread(n):
    for i in range(n):
        get("2016-04-04", "JYK", "BJP", "15:00", "22:00")
        # lock.acquire()
        # try:
        #     get("2016-04-04", "JYK", "BJP", "15:00", "22:00")
        # finally:
        # lock.release()


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    s = [["0", "2016-04-04", "JYK", "BJP", "15:00", "22:00"],
         ["1", "2016-05-02", "JYK", "BJP", "15:00", "22:00"],
         ["2", "2016-04-04", "HIK", "BJP", "15:00", "22:00"],
         ["3", "2016-05-02", "HIK", "BJP", "15:00", "22:00"]]

    for i in range(4):
        p.apply_async(get, args=(s[i]))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
