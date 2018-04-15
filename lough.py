#_*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
from lxml import etree
import json

import requests


class Tencen_Spider(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/8hr/page/'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.list = []
        # 发送请求

    def send_request(self, url, params={}):
        try:
            data = requests.get(url, headers=self.headers).content
            return data
        except Exception, err:
            print err

    # 数据解析
    def analy(self, data):
        # 转换类型
        soup = BeautifulSoup(data, 'lxml')
        # 先取出所有的子div
        child = soup.select('#content-left .article')
        # 循环获取内容
        for i in child:
            dict = {}
            # 昵称
            dict['name'] = i.select('.author h2')[0].get_text().strip()
            # 点赞
            dict['sat'] = i.select('.stats i')[0].get_text().strip()

            # 正文
            dict['con'] = i.select('.content span')[0].get_text().strip()
            ferr=i.select('.articleGender')
            if ferr:
            # 年龄
                dict['age'] = i.select('.articleGender')[0].get_text()
                # 性别
                dict['sex'] = i.select('.articleGender')[0].get('class')[1].replace('Icn', '')
            else:
                dict['age'] ='无'
                dict['sex'] ='无'
            self.list.append(dict)

    # 写入本地文件
    def write_file(self):
        data_str = json.dumps(self.list)
        with open('07.json', 'w') as f:
            f.write(data_str)

    # 调度
    def start_work(self):
        for page in range(1, 5):
            url = self.base_url + str(page)

        # 2.发送请求
        data = self.send_request(url)

        # 3.解析
        self.analy(data)
        # 4. 存html .json
        self.write_file()


if __name__ == '__main__':
    tool = Tencen_Spider()
    tool.start_work()
