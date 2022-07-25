#!/usr/bin/env python3
# encoding=utf8
'''
番剧订阅主流程
'''

import feedparser
import db
import config
import datetime
import time
import requests

class Bangumi(object):

    def __init__(self,name,season,stream,filename_reg,status,last_time,cron,download,archive,rename_type,bangumi_id=0) -> None:
        self.name=name
        self.season=season
        self.stream=stream
        self.filename_reg=filename_reg
        self.status=status
        self.last_time=last_time
        self.cron=cron
        self.download=download
        self.archive=archive
        self.rename_type=rename_type
        self.bangumi_id=bangumi_id

    @staticmethod
    def initFromDatabase(bangumi_id):
        with db.Database() as conn:
            pass
