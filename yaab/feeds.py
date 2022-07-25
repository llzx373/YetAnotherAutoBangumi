#!/usr/bin/env python3
# encoding=utf8
'''
订阅feed流代码
'''

import feedparser
import db
import config
import datetime
import time
import requests

class Stream(object):

    def __init__(self, name,stream_type, url,status, cron, last_time,) -> None:
        self.name = name
        self.url = url
        self.cron = cron
        self.status = status
        self.last_time = last_time
        self.stream_type=stream_type

    @staticmethod
    def initFromDatabase(name):
        with db.Database() as conn:
            objs = conn.select("select name,stream_type,url,status,cron,last_time from stream where name =%s",(name,))
            if len(objs)!=1:
                raise Exception("not exist.")
            obj=objs[0]
            return Stream(obj['name'],obj['stream_type'],obj['url'],obj['status'],obj['cron'],obj['last_time'])

    @staticmethod
    def newStream(stream):
        with db.Database() as conn:
            conn.execute('''insert into stream(name,stream_type,url,status,cron,last_time) 
            values(%s,%s,%s,%s,%s,%s)''',(stream.name,stream.stream_type,stream.url,stream.status,stream.cron,stream.last_time)
            )
    
    def update(self):
        with db.Database() as conn:
            pass
    
    def delete(self):
        with db.Database() as conn:
            if self.stream_id == 0:
                raise Exception("try delete id 0 FeedStream")
            conn.execute("delete from feed_stream where stream_id = ?",(self.stream_id,))
        
    def flush(self):
        '''
        这里刷新feed
        1. 获取url
        2. 解析feed记录
        3. 计算唯一标记
        4. 如果当前不存在，则插入种子表
        5. 更新最后更新时间
        6. 如果出错修改status
        '''
        if self.stream_type =='dmhy':
            response = requests.get(self.url,proxies=config.proxies)
            steam_rss=feedparser.parse(response.text)
            with db.Database() as conn:
                for entry in steam_rss['entries']:
                    torrent=None
                    for link in entry['links']:
                        if link['type']=='application/x-bittorrent':
                            torrent=link['href']
                    conn.execute('''insert into torrent (feed_id,title,url,status,add_time,stream,tags)
                        values(%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE NOTHING''',
                        (entry['id'],entry['title'],torrent,'INIT',datetime.datetime.fromtimestamp(time.mktime(entry['published_parsed'])),
                        self.name,str(entry['tags']))
                    )
    
if __name__ =='__main__':
    # stream=Stream("dmhy","https://share.dmhy.org/topics/rss/rss.xml","1h",'active',datetime.datetime.now(),"rss")
    # Stream.newStream(stream)
    stream=Stream.initFromDatabase("dmhy")
    stream.flush()