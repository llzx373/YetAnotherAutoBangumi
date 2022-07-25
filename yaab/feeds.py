#!/usr/bin/env python3
# encoding=utf8
'''
订阅feed流代码
'''
from py_compile import main
import db
import config

'''
create sequence feed_stream_id;

create table feed_stream 
(
    int stream_id,
    name varchar,
    stream_type varchar,
    url text,
    status varchar,
    cron varchar,
    last_time date,
    primary key(name)
)
'''


class FeedStream(object):

    def __init__(self, name, url, cron, status, last_time,stream_type, stream_id=0) -> None:
        self.name = name
        self.url = url
        self.cron = cron
        self.status = status
        self.last_time = last_time
        self.stream_type=stream_type
        self.stream_id = stream_id

    @staticmethod
    def initFromDatabase(self, stream_id):
        with db.Database(config.pg_conninfo) as conn:
            pass

    @staticmethod
    def newFeedStream(self, feedStream):
        with db.Database(config.pg_conninfo) as conn:
            pass
    
    def update(self):
        with db.Database(config.pg_conninfo) as conn:
            pass
    
    def delete(self):
        with db.Database(config.pg_conninfo) as conn:
            if self.stream_id == 0:
                raise Exception("try delete id 0 FeedStream")
            conn.execute("delete from feed_stream where stream_id = ?",(self.stream_id,))
    
if __name__ =='__main__':
    pass