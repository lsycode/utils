# python 3.4
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import webbrowser
import urllib.request

url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
# url = "http://www.baidu.com"

# h ={
# GET /otn/confirmPassenger/initDc HTTP/1.1
# Host: kyfw.12306.cn
# Connection: keep-alive
# Pragma: no-cache
# Cache-Control: no-cache
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36
# Accept-Encoding: gzip, deflate, sdch
# Accept-Language: zh-CN,zh;q=0.8
# Cookie: __NRF=FA416421DBC6E5BD6B265E0F97661C4D; JSESSIONID=0A01D491987EE7ADC8ED36D3BFECD490061708ECF9; BIGipServerotn=2446590218.38945.0000; BIGipServerportal=3151233290.17695.0000; _jc_save_fromStation=%u5DE8%u91CE%2CJYK; _jc_save_toStation=%u5317%u4EAC%2CBJP; _jc_save_fromDate=2016-04-08; _jc_save_toDate=2016-03-24; _jc_save_wfdc_flag=dc; current_captcha_type=Z
#
#
# }
h = {
    "Host": "kyfw.12306.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cookie": "__NRF=FA416421DBC6E5BD6B265E0F97661C4D; JSESSIONID=0A01D491987EE7ADC8ED36D3BFECD490061708ECF9; BIGipServerotn=2446590218.38945.0000; BIGipServerportal=3151233290.17695.0000; _jc_save_fromStation=%u5DE8%u91CE%2CJYK; _jc_save_toStation=%u5317%u4EAC%2CBJP; _jc_save_fromDate=2016-04-08; _jc_save_toDate=2016-03-24; _jc_save_wfdc_flag=dc; current_captcha_type=Z"
}
# data = {}
# #req = urllib.request.Request(url)
req = urllib.request.Request(url, headers=h)
data = urllib.request.urlopen(req).read()
data = data.decode('gbk')
print(data)
with open(r'C:\Users\andy\Desktop\crawler.html', 'w', encoding='utf-8') as f:
    f.write(str(data))
