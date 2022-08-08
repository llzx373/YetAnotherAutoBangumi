#encoding=utf8

'''
流程步骤：

1. 获取rss # 这一步要在单个rss订阅内，可以获取到所有历史番剧才行，dmhy中订阅连载需要带过滤条件，全量追踪后续想办法。
2. 进行过滤 # 这一步后，应该只剩下需要下载的种子，如果多出来，就也会被下载。
3. 放入torrent文件夹 # 如果当前种子文件已经存在，则不操作，如果不存在，就放进去，名字是maglink的md5.torrent。
4. 获取下载目录列表  # 获取整个下载目录文件列表（walk）
5. 如果发现名称匹配,进行指定的硬连接处理，如果硬连接目标已经有文件，则不处理。
'''

import re
import feedparser
import requests
import os

from config import proxies,bangomis,downloads,qbittorrent_attr
import shutil
import libtorrent as lt
import tempfile
import time
import qbittorrent

def magnet2torrent(magnet):
    tempdir = tempfile.mkdtemp()
    ses = lt.session()
    params = {
        'save_path': tempdir,
        'storage_mode': lt.storage_mode_t(2),
    }
    handle = lt.add_magnet_uri(ses, magnet, params)

    while (not handle.has_metadata()):
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            ses.pause()
            shutil.rmtree(tempdir)
            return None
    ses.pause()
    torinfo = handle.get_torrent_info()
    torfile = lt.create_torrent(torinfo)
    rt= lt.bencode(torfile.generate())
    ses.remove_torrent(handle)
    shutil.rmtree(tempdir)
    return rt

def torrents(title,href,torrent_path):
    magnetName = href[href.find("btih:") + 1:href.find("&")]
    magnetName = magnetName.replace('tih:','').lower()

    if not os.path.exists(torrent_path):
        os.makedirs(torrent_path)
    output = f"{torrent_path}/{magnetName}.torrent"
    if os.path.exists(output):
        return
    if os.path.exists(output+".qbt_rejected"):
        return
    if os.path.exists(f"{downloads}/{magnetName}.torrent"):
        return
    print("rss file:",title,output)
    os.chdir(torrent_path)

    torrent_data = magnet2torrent(href)
    with open(output,'wb') as f:
        f.write(torrent_data)
    with open(f"{downloads}/{magnetName}.torrent",'wb') as f:
        f.write(torrent_data)

class Bangumi(object):

    def __init__(self,name,rss_link,rss_patten,torrent_path,download_path,season,link_patten,link_path) -> None:
        self.name = name
        self.rss_link = rss_link
        self.rss_patten = rss_patten
        self.torrent_path = torrent_path
        self.download_path = download_path
        self.season = season
        self.link_patten = link_patten
        self.link_path = link_path

    def rss(self):
        response = requests.get(self.rss_link,proxies=proxies)
        steam_rss=feedparser.parse(response.text)
        for entry in steam_rss['entries']:
            for link in entry['links']:
                if link['type']=='application/x-bittorrent':
                    print("rss get:",entry['title'])
                    yield entry['title'],link['href']

    def rss_filter(self):
        for title,href in self.rss():
            if re.search(self.rss_patten,title):
                print("rss filter:",title)
                yield title,href

    def get_torrents(self):
        qb = qbittorrent.Client(qbittorrent_attr['url'])
        qb.login(qbittorrent_attr['username'],qbittorrent_attr['password'])
        torrents = qb.torrents(filter='all')
        torrents={ torrent['hash']:torrent
            for torrent in torrents
        }
        for title,href in self.rss_filter():
            hash_info = href[href.find("btih:") + 1:href.find("&")]
            hash_info = hash_info.replace('tih:','').lower()
            if hash_info not in torrents:
                qb.download_from_link(href)
                



    def downloaded(self):
        for root, dirs, files in os.walk(self.download_path):
            for name in files:
                print(root,name,self.link_patten)
                print(re.findall(self.link_patten,name))
                if re.findall(self.link_patten,name):
                    episode = re.findall(self.link_patten,name)[0]
                    yield root+'/'+name,episode


    def rename(self):
        for download,episode in self.downloaded():
            if self.season == None:
                self.season = 1
            season = self.season
            if season < 10:
                season='0'+str(season)
            else:
                season=str(season)
            file_ex=download.split('.')[-1]
            dest_path = f'{self.link_path}/{self.name}/Season {season}'
            dest_episode = f'{dest_path}/{self.name} S{season}E{episode}.{file_ex}'
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            if os.path.exists(dest_episode):
                continue
            else:
                os.link(download,dest_episode)

if __name__ =='__main__':
    for bangumi_attr in bangomis:
        bangumi = Bangumi(**bangumi_attr)
        bangumi.get_torrents()
        bangumi.rename()