# coding=utf-8
import requests
from lxml import etree
import os
import re


class TieBa(object):
    """抓取百度贴吧美女图片"""
    def __init__(self, word):
        self.url = 'https://tieba.baidu.com/f?kw={}'.format(word)  # 
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; TUCOWS) '
        }    # 设置浏览器

    def get_data(self, url):
        # 构造请求
        response = requests.get(url, headers=self.headers)
        data = response.content
        # print(data)
        return data

    def parse_page(self, data):
        """解析数据"""
        # 创建xpath对象
        html = etree.HTML(data)
        # 提取当前页标题，url数据
        node_list = html.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a')
        detail_list = []
        for node in node_list:
            temp = dict()
            temp['title'] = node.xpath('./text()')[0]
            temp['url'] = 'https://tieba.baidu.com' + node.xpath('./@href')[0]
            detail_list.append(temp)
            # print(temp)
        # 提取下一页连接
        next_url = html.xpath('//*[@id="frs_list_pager"]/a[contains(text(), "下一页")]/@href')[0]
        next_url = 'http:' + next_url if len(next_url) > 0 else None
        # print(next_url)
        return detail_list, next_url

    def parse_detail(self, detail_list):
        """提取详情页url"""
        data_url = []
        for detail in detail_list:
            data_url.append(detail['url'])
        return data_url

    def save_data(self, url):
        """保存数据"""
        # 请求标题连接地址
        data = self.get_data(url)
        # 创建xpath对象
        html = etree.HTML(data)
        # print(html)
        # print(url)
        # 获取图片url
        try:
            image_url = html.xpath('//*[contains(@id,"post_content")]/img[1]/@src')[0]
        except Exception as e:
            return
        print(image_url)
        # 判断图片地址是否已jpg结尾
        if re.match(r'.*\.jpg$', image_url):
            # 请求图片地址，获取图片
            image_data = self.get_data(image_url)
            filename = '美女吧图片/' + image_url.split('/')[-1]
            # print(filename)
            # 保存图片
            with open(filename, 'wb') as f:
                f.write(image_data)

    def run(self):
        # 判断是否有image文件夹
        if not os.path.exists('美女吧图片'):   
            # 创建文件夹
            os.mkdir('美女吧图片')
        next_url = self.url  # https://tieba.baidu.com/f?kw=美女
        # 请求美女吧首页
        data = self.get_data(next_url)
        # 保存首页文件，观察数据，是否有需要的数据
        with open('tieba.json', 'wb') as f:
            f.write(data)
        # 如果有下一页就执行
        while next_url:
            # 获取每页标题和对应的连接地址
            detail_list, next_url = self.parse_page(data)
            # 提取每页的详情页的url
            data_url = self.parse_detail(detail_list)
            # 遍历每个url
            for url in data_url:
                # 保存图片
                self.save_data(url)
            # 构造下一页请求
            data = self.get_data(next_url)


if __name__ == '__main__':
    tb = TieBa('美女')
    tb.run()
