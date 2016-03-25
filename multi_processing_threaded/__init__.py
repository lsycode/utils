# python 3.4
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import http.client
import urllib.request
import urllib.parse, time, random
import os
from multiprocessing import Pool


def connect():
    url = "http://www.baidu.com"

    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')

    print("suc")


def long_time_task(name):
    for i in range(3):
        print('Run task %s (%s)...' % (name, os.getpid()))
        start = time.time()
        time.sleep(random.random() * 3)
        end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
