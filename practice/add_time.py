import os
path = r'E:\WeiLai\OneDrive\blog\source\_posts'
filess = os.listdir(path)
for files in filess:
    file_path = path + '\\' + files
    mds = os.listdir(file_path)
    for md in mds:
        if 'md' in md:
            doc = file_path +'\\'+ md
            with open (doc,'a') as f:
                f.write('date: 2018-10-24 22:53:08') # 写在了最后面
                ##  写时间  date = 创建时间
                ##  时间格式
'''
---
title: VPS搭建SSR过程
date: 2018-10-24 22:53:08
tags:
categories: VPS
---

'''
