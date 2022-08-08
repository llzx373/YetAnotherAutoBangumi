#encoding=utf8

proxies = {
   'http': 'http://192.168.1.21:7890',
   'https': 'http://192.168.1.21:7890',
}

qbittorrent_attr={
    'url':"http://127.0.0.1:8080",
    'username':'admin',
    'password':'passwd'
}
torrent_path='/data7/Auto_Bangumi/torrents'
download_path='/data7/Auto_Bangumi/downloads'
link_path='/data7/Auto_Bangumi/links'
rss_prefix='https://share.dmhy.org/topics/rss/rss.xml?'
bangomis= [
    {
        'name':"莉可丽丝",
        'rss_link':rss_prefix+"keyword=Lycoris+Recoi&sort_id=0&team_id=803&order=date-desc",
        'rss_patten':'CHT',
        'torrent_path':'/data7/Auto_Bangumi/torrents',
        'download_path':'/data7/Auto_Bangumi/downloads',
        'season':None,
        'link_patten':"Lilith.*Lycoris Recoil - ([\d]+) \[Baha\].*mp4",
        'link_path':"/data7/Auto_Bangumi/links"
    },
    {
        'name':"契约之吻",
        'rss_link':"https://share.dmhy.org/topics/rss/rss.xml?keyword=%E5%A5%91%E7%BA%A6%E4%B9%8B%E5%90%BB&sort_id=0&team_id=803&order=date-desc",
        'rss_patten':'Baha',
        'torrent_path':'/data7/Auto_Bangumi/torrents',
        'download_path':'/data7/Auto_Bangumi/downloads',
        'season':None,
        'link_patten':"Engage Kiss - ([\d]+).*mp4",
        'link_path':"/data7/Auto_Bangumi/links"
    },
    {
        'name':"异世界归来的舅舅",
        'rss_link':"https://share.dmhy.org/topics/rss/rss.xml?keyword=%E8%88%85%E8%88%85+1080+%E7%AE%80%E4%BD%93&sort_id=0&team_id=619&order=date-desc",
        'rss_patten':'1080',
        'torrent_path':'/data7/Auto_Bangumi/torrents',
        'download_path':'/data7/Auto_Bangumi/downloads',
        'season':None,
        'link_patten':"Isekai Ojisan \[(\d+)\].*mp4",
        'link_path':"/data7/Auto_Bangumi/links"
    },
    {
        'name':"徹夜之歌",
        'rss_link':"https://share.dmhy.org/topics/rss/rss.xml?keyword=%E5%BE%B9%E5%A4%9C%E4%B9%8B%E6%AD%8C+%E7%AE%80&sort_id=0&team_id=731&order=date-desc",
        'rss_patten':'1080',
        'torrent_path':'/data7/Auto_Bangumi/torrents',
        'download_path':'/data7/Auto_Bangumi/downloads',
        'season':None,
        'link_patten':"Yofukashi no Uta\]\[(\d+)\].*mp4",
        'link_path':"/data7/Auto_Bangumi/links"
    },
    {
        'name':"神渣☆偶像",
        'rss_link':"https://share.dmhy.org/topics/rss/rss.xml?keyword=Kami+Kuzu&sort_id=0&team_id=803&order=date-desc",
        'rss_patten':'1080',
        'torrent_path':'/data7/Auto_Bangumi/torrents',
        'download_path':'/data7/Auto_Bangumi/downloads',
        'season':None,
        'link_patten':"dol - ([\d]+) .*mp4",
        'link_path':"/data7/Auto_Bangumi/links"
    },
    {
        'name':"金装的薇尔梅",
        'rss_link':"https://share.dmhy.org/topics/rss/rss.xml?keyword=Kinsou+no+Vermeil+1080+%E7%AE%80&sort_id=0&team_id=669&order=date-desc",
        'rss_patten':'1080',
        'torrent_path':'/data7/Auto_Bangumi/torrents',
        'download_path':'/data7/Auto_Bangumi/downloads',
        'season':None,
        'link_patten':"Kinsou no Vermeil\]\[([\d]+)\].*mp4",
        'link_path':"/data7/Auto_Bangumi/links"
    },
    {
        'name':"传颂之物 二人的白皇",
        'rss_link':"https://share.dmhy.org/topics/rss/rss.xml?keyword=Utawarerumono+B&sort_id=0&team_id=801&order=date-desc",
        'rss_patten':'1080',
        'torrent_path':'/data7/Auto_Bangumi/torrents',
        'download_path':'/data7/Auto_Bangumi/downloads',
        'season':None,
        'link_patten':"白皇 - ([\d]+) .*mkv",
        'link_path':"/data7/Auto_Bangumi/links"
    },
    {
        'name':"影宅",
        'rss_link':rss_prefix+'keyword=Shadows+House+2nd+B&sort_id=0&team_id=801&order=date-desc',
        'rss_patten':'1080',
        'torrent_path':torrent_path,
        'download_path':download_path,
        'season':2,
        'link_patten':"影宅 第二季 - ([\d]+) .*mkv",
        'link_path':link_path
    }

]

downloads = "/data7/Auto_Bangumi/app/data"
