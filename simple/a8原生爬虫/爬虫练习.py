from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
).read().decode('utf-8')
# print(html)
# '''
# <!DOCTYPE html>
# <html lang="cn">
# <head>
#         <meta charset="UTF-8">
#         <title>Scraping tutorial 1 | 莫烦Python</title>
#         <link rel="icon" href="https://morvanzhou.github.io/static/img/description/tab_icon.png">
# </head>
# <body>
#         <h1>爬虫测试1</h1>
#         <p>
#                 这是一个在 <a href="https://morvanzhou.github.io/">莫烦Python</a>
#                 <a href="https://morvanzhou.github.io/tutorials/data-manipulation/scraping/">爬虫教程</a> 中的简单测试.
#         </p>

# </body>
# </html>
# '''

import re
res = re.findall(r"<title>(.+?)</title>", html) 
print(res)  # ['Scraping tutorial 1 | 莫烦Python'] # 列表
print(res[0]) # Scraping tutorial 1 | 莫烦Python
res = re.findall(r"<p>(.*?)</p>", html)
print(res) 

res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print(res)
print(res[0]) 
'''
# Page paragraph is:
#                 这是一个在 <a href="https://morvanzhou.github.io/">莫烦Python</a>
#                 <a href="https://morvanzhou.github.io/tutorials/data-manipulation/scraping/">爬虫教程</a> 中的简单测试.
# '''
res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)
# '''
# beautifulSoup
# 1. 选择要爬的网址 (url)
# 2. 使用 python 登录上这个网址 (urlopen等)
# 3. 读取网页信息 (read() 出来)
# 4. 将读取的信息放入 BeautifulSoup
# 5. 使用 BeautifulSoup 选取 tag 信息等 (代替正则表达式)
'''
# from bs4 import BeautifulSoup
# from urllib.request import urlopen


# # if has Chinese, apply decode()
# html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
# print(html)
# '''
# 取这个网页信息, 我们将要加载进 BeautifulSoup, 以 lxml 的这种形式加载. 除了 lxml, 
# 其实还有很多形式的解析器, 不过大家都推荐使用 lxml 的形式.
# 然后 soup 里面就有着这个 HTML 的所有信息. 如果你要输出 <h1> 标题, 可以就直接 soup.h1.

# '''

# soup = BeautifulSoup(html, features='lxml')
# print(soup.h1)  # <h1>爬虫测试1</h1>   # 读取标签

# print('\n', soup.p)

# """
# <p>
# 		这是一个在 <a href="https://morvanzhou.github.io/">莫烦Python</a>
# <a href="https://morvanzhou.github.io/tutorials/scraping">爬虫教程</a> 中的简单测试.
# 	</p>
# """

# '''
# 使用 BeautifulSoup,使用 CSS 的 Class 来选择内容
# CSS 主要用途就是装饰你 “骨感” HTML 页面.
# '''
