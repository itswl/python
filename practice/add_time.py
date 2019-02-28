# import os
# import sys
# import time

# path = r'E:\WeiLai\OneDrive\blog\source\_posts'
# filess = os.listdir(path)
# for files in filess:
#     file_path = path + '\\' + files
#     mds = os.listdir(file_path)
#     for md in mds:
#         if 'md' in md:
#             full_path = file_path +'\\'+ md
#             mtime = os.stat(full_path).st_mtime
#             file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
            

                #  写时间  date = 创建时间
                #  时间格式
'''
---
title: VPS搭建SSR过程
date: 2018-10-24 22:53:08
tags:
categories: VPS
---

'''
import os
import sys
import time

path = r'E:\WeiLai\OneDrive\blog\source\_posts'
for root, dir, files in os.walk(path):
    for file in files:
        full_path = os.path.join(root, file)
        if '.md' in full_path:
            mtime = os.stat(full_path).st_mtime
            file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
            date = 'date: '+file_modify_time

            with open (full_path,'r', encoding='UTF-8') as f:
                s = f.read()
                q = s.partition('tags:')       
                t = q[0] + date +'\n' + q [1] + q[2]
                with open (full_path,'w', encoding='UTF-8') as f:
                    f.write(t)

            


    