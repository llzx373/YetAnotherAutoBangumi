#!/usr/bin/env python3
#encoding=utf8
'''
参数配置
'''

pg_conninfo = "host=192.168.1.21 port=15432 user=app password=Qwer1234 dbname=autobangumi"

proxies = {
   'http': 'http://192.168.1.21:7890',
   'https': 'http://192.168.1.21:7890',
}