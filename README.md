# 另一个自动追番工具

目标是写个重随时追番体验的自动番组下载工具。

受到项目AutoBangumi(https://github.com/EstrellaXD/Auto_Bangumi)的启发。

在其设计思想基础上，进行简化，单纯做种子追踪+刮削重命名。

其中重命名部分采用linux硬连接而非直接rename，一来避免qbittorrent识别不到已经下载的番剧，二来也方便万一刮削错误可以重置。

# 主要逻辑

config文件中，配置代理，qbittorrent连接参数，番剧列表配置（预制为作者自己的追番表）。

之所以使用编程文件而非配置文件作为配置，主要目的是方便更灵活的控制。
```python
{
    'name':"莉可丽丝",
    'rss_link':rss_prefix+"keyword=Lycoris+Recoi&sort_id=0&team_id=803&order=date-desc",
    'rss_patten':'CHT',
    'torrent_path':'/data7/Auto_Bangumi/torrents',
    'download_path':'/data7/Auto_Bangumi/downloads',
    'season':None,
    'link_patten':"Lilith.*Lycoris Recoil - ([\d]+) \[Baha\].*mp4",
    'link_path':"/data7/Auto_Bangumi/links"
}
```
name：番剧名称，也是刮削的目标名称，需要在tmdb，tvdb等预期的元数据库中可以查到。
rss_link:大马哈鱼（dmhy）的rss订阅连接，虽然下方有rss_patten作为过滤条件，但还是推荐在rss_link中就预设好条件，这样处理也方便。
rss_patten：对于种子名称进行二次过滤，避免rss的搜索条件覆盖不到的一些场景，此处为正则表达式。
torrent_path：暂时废弃字段，早期设定为独立于下载器的torrent目录（这种方式可以兼容于几乎所有bt下载器），但因为从maglink获取种子有些麻烦，因此废弃，而采用直接调用qbittorrent的方式。
download_path：下载路径，仅用于刮削，应该配置为qb的默认下载目录。
season：第几季，用于刮削时候season的设定，如果为空默认为第一季。
link_patten：用于刮削时候获取第几集，其中()用于提取对应集的数字。这个表达式会作用于所有下载目录下的文件，建议写作时候区分度大些，避免识别错误。
link_path：硬连接的目标位置。

# 新番下载

在上述配置完成，并且依赖安装完整的情况下，增加crontab：

0 * * * * /data7/Auto_Bangumi/app/venv/bin/python /data7/Auto_Bangumi/app/yaab/app.py 2>&1 >> /data7/Auto_Bangumi/app/app.log
# 完结番剧重命名

renamer.py

主要用于番剧重命名：

renamer.py {番剧刮削名称} {季} {集获取正则表达式} {原始文件目录} {硬连接目录}

example：

python /data7/Auto_Bangumi/renamer.py '女武神驱动 美人鱼' 01 '-MERMAID- \[([\d]+)\].*' '/data7/data/新番/女武神驱动' /data7/Auto_Bangumi/links

# 运行效果

作为cron跑两周的效果如下：
```bash
tree -N /data7/Auto_Bangumi/links

/data7/Auto_Bangumi/links
├── 徹夜之歌
│   └── Season 01
│       ├── 徹夜之歌 S01E01.mp4
│       ├── 徹夜之歌 S01E02.mp4
│       ├── 徹夜之歌 S01E03.mp4
│       ├── 徹夜之歌 S01E04.mp4
│       └── 徹夜之歌 S01E05.mp4
├── 传颂之物 二人的白皇
│   └── Season 01
│       ├── 传颂之物 二人的白皇 S01E01.mkv
│       ├── 传颂之物 二人的白皇 S01E02.mkv
│       ├── 传颂之物 二人的白皇 S01E03.mkv
│       ├── 传颂之物 二人的白皇 S01E04.mkv
│       ├── 传颂之物 二人的白皇 S01E05.mkv
│       ├── 传颂之物 二人的白皇 S01E06.mkv
│       └── 传颂之物 二人的白皇 S01E07.mkv
├── 金装的薇尔梅
│   └── Season 01
│       ├── 金装的薇尔梅 S01E01.mp4
│       ├── 金装的薇尔梅 S01E02.mp4
│       ├── 金装的薇尔梅 S01E03.mp4
│       ├── 金装的薇尔梅 S01E04.mp4
│       └── 金装的薇尔梅 S01E05.mp4
├── 莉可丽丝
│   └── Season 01
│       ├── 莉可丽丝 S01E01.mp4
│       ├── 莉可丽丝 S01E02.mp4
│       ├── 莉可丽丝 S01E03.mp4
│       ├── 莉可丽丝 S01E04.mp4
│       ├── 莉可丽丝 S01E05.mp4
│       └── 莉可丽丝 S01E06.mp4
├── 契约之吻
│   └── Season 01
│       ├── 契约之吻 S01E01.mp4
│       ├── 契约之吻 S01E02.mp4
│       ├── 契约之吻 S01E03.mp4
│       ├── 契约之吻 S01E04.mp4
│       ├── 契约之吻 S01E05.mp4
│       └── 契约之吻 S01E06.mp4
├── 神渣☆偶像
│   └── Season 01
│       ├── 神渣☆偶像 S01E01.mp4
│       ├── 神渣☆偶像 S01E02.mp4
│       ├── 神渣☆偶像 S01E03.mp4
│       ├── 神渣☆偶像 S01E04.mp4
│       ├── 神渣☆偶像 S01E05.mp4
│       └── 神渣☆偶像 S01E06.mp4
├── 异世界归来的舅舅
│   └── Season 01
│       ├── 异世界归来的舅舅 S01E01.mp4
│       ├── 异世界归来的舅舅 S01E02.mp4
│       ├── 异世界归来的舅舅 S01E03.mp4
│       └── 异世界归来的舅舅 S01E04.mp4
├── 影宅
│   └── Season 02
│       ├── 影宅 S02E01.mkv
│       ├── 影宅 S02E02.mkv
│       ├── 影宅 S02E03.mkv
│       ├── 影宅 S02E04.mkv
│       └── 影宅 S02E05.mkv
```