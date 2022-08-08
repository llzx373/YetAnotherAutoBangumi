#encoding=utf8

import sys
import os
import re

'''
renamer.py title season reg source dest
'''

if __name__ =='__main__':
    title=sys.argv[1]
    season=sys.argv[2]
    reg=sys.argv[3]
    source=sys.argv[4]
    dest=sys.argv[5]

    for root,dirs,files in os.walk(source):
        for filename in files:
            if re.findall(reg,filename):
                episode= re.findall(reg,filename)[0]
                file_ex=filename.split('.')[-1]
                dest_episode = f'{dest}/{title}/Season {season}/{title} S{season}E{episode}.{file_ex}'
                dest_path = f'{dest}/{title}/Season {season}'
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                if os.path.exists(dest_episode):
                    continue
                else:
                    source_filename=root+'/'+filename
                    os.link(source_filename,dest_episode)