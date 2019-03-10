
import re
import requests
from requests.exceptions import RequestException
import sys
import io
import pandas as pd
import csv
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # 改变标准输出的默认编码


def get_page(url):
    try:
        headers = {
            'User-Agent': 'User-Agent  Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        }
        response = requests.get(url, headers=headers
                                )
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        print('获取错误')
        return None


def page_info(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find_all('tr', {'class': 'tr3 t_one'})
    # print(trs)
    for tr in trs:
        try:
            a = tr.find_all('a', {'class': 'subject'})
            # print(a)
            text = a[0].get_text()
            # print(text)
            if 'club' in text:
                print(a)

        except Exception:
            return None
        # name = a.find_all('a')
        # print(name)


if __name__ == '__main__':
    for i in range(200, 380):
        i = str(i)
        html = get_page('http://yewo2048.info/2048/thread.php?fid-16-page-' + i + '.html')
        page_info(html)
