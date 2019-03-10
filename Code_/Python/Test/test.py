'''

import requests

# 不加请求头，
# 会被识别为这是一个爬虫，所以需要加入请求头伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
url = 'http://httpbin.org/get'
html = requests.get(url, headers=headers)
print(html.text)


import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import sys
import io
import re
import pandas as pd
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # 改变标准输出的默认编码


def get_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('获取错误')
        return None


def parse_page(html):
    soup = BeautifulSoup(html, 'lxml')
    books_left = soup.find('ul', {'class': 'cover-col-4 clearfix'})
    books_left = books_left.find_all('li')

    books_right = soup.find('ul', {'class': 'cover-col-4 pl20 clearfix'})
    books_right = books_right.find_all('li')

    books = list(books_left) + list(books_right)
    return books


def save_as_list(books):
    img_urls = []
    titles = []
    ratings = []
    authors = []
    details = []

    for book in books:
        img_url = book.find_all('a')[0].find('img').get('src')
        img_urls.append(img_url)

        title = book.find_all('a')[1].get_text()
        titles.append(title)

        rating = book.find('p', {'class': 'rating'}).get_text()
        ratings.append(rating)

        # author = book.find('p', {'class': 'color-gray'}).get_text()
        author = book.find_all('p')[1].get_text()
        authors.append(author)
        #???为什么detail 不可以使用class 查找到
        detail = book.find_all('p')[2].get_text()
        details.append(detail)

    return img_urls, titles, authors, details


def save_as_csv(result, img_urls, titles, authors, details):
    result = pd.DataFrame()
    result['img_urls'] = img_urls
    result['titles'] = titles
    result['authors'] = authors
    result['details'] = details
    result.to_csv('result.csv', index=None, encoding='utf_8_sig')


def main():
    url = 'https://book.douban.com/latest'
    html = get_page(url)
    books = parse_page(html)
    img_urls, titles, authors, details = save_as_list(books)
    save_as_csv(img_urls, titles, authors, details)


if __name__ == '__main__':
    main()

    通过使用bs4 中的BeautifulSoup()用'lxml'方式解析代码

'''

# 在获取网站时的代码错误

import requests
from requests.exceptions import RequestException

urls = ['http://www.hao123.com', 'http://www.baidussss.com', 'http://ww.we.com']


def get_html(url):
    try:
        response = requests.get(url)

    except requests.exceptions.ConnectionError as e:
        print('错误详情', e)
        return None


def run(url):
    get_html(url)


if __name__ == '__main__':
    for url in urls:
        get_html(url)
