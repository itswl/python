from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

import pymysql.cursors   # 数据库


base_url = "https://baike.baidu.com"
his = ["/item/%E5%8F%B2%E8%AE%B0"]

for i in range(1000):
    # dealing with Chinese symbols
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')

    print(i, soup.find('h1').get_text(), '    url: ', url)

    # find valid urls
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        his.pop()

# 链接数据库
    connection = pymysql.connect(host = 'localhost',
                user = 'root',
                password = 'password',
                db = 'baikeurl',
                charset = 'utf8mb4',
                     )

    try:
        # 获取会话指针
        with connection.cursor() as cursor:
            # 创建sql 语句
            sql = 'insert into `urls`(`urlname`,`urlhref`)values(%s,%s)'
            # 执行sql 语句
            cursor.execute(sql,(soup.find('h1').get_text(),url))
            # 提交
            connection.commit()
    except:
        pass 
    finally:
        connection.close()

# 查询数据库
'''
cursor.execute()   得到总记录数
cursor.fetchone()  查询下一行
cursor.fetchmany(size=None)   得到指定大小
cursor.fetchall    得到全部
 
'''