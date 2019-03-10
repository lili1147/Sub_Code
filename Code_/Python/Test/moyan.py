'''
1.使用正则表达式爬取信息，猫眼榜单TOP100
并保存到csv文件中
'''

import re
import requests
from requests.exceptions import RequestException
import sys
import io
import pandas as pd
import csv
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # 改变标准输出的默认编码


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'User-Agent  Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('获取错误')
        return None


def parse_one_page(html):
    # pattern = re.compile(
    #     '<dd>.*?board-index.*?>(.*?)</i>.*?<a.*?title="(.*?)".*?board-img.*?src="(.*?)"', re.S)
    # movies = re.findall(pattern, html)
    # print(movies)
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?<a.*?title="(.*?)".*?data-src="(.*?)".*?board-img.*?'
                         '<p.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?<i.*?integer">(.*?)</i>.*?fraction">(.*?)</i>'
                         '.*?</dd>', re.S)

    items = re.findall(pattern, html)
    indexs = []
    titles = []
    img_srcs = []
    stars = []
    dates = []
    scores = []

    for movie in items:
        indexs.append(movie[0])
        titles.append(movie[1])
        img_srcs.append(movie[2])
        stars.append(movie[3].strip())
        dates.append(movie[4])
        scores.append(movie[5] + movie[6])

    return indexs, titles, img_srcs, stars, dates, scores


def save_as_csv(indexs, titles, img_srcs, stars, dates, scores):
    f = open('moyan.csv', 'a', encoding='utf-8')
    moyan = pd.DataFrame()
    moyan[0] = indexs
    moyan[1] = titles
    moyan[2] = img_srcs
    moyan[3] = stars
    moyan[4] = dates
    moyan[5] = scores

    moyan.to_csv(f, mode='a', index=None, encoding='utf-8_sig', header=False)


def run(offset):

    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    indexs, titles, img_srcs, stars, dates, scores = parse_one_page(html)

    save_as_csv(indexs, titles, img_srcs, stars, dates, scores)


if __name__ == '__main__':
    f = open('moyan.csv', 'w', encoding='utf_8_sig', newline='')
    writer = csv.writer(f)
    writer.writerow(['index', 'title', 'img-src', 'star', 'score'])
    f.close()
    for i in range(10):
        run(i * 10)
