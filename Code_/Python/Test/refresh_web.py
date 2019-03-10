'''
当遇到网速不好时，一般等待一会再刷新网页即可。模拟这个过程

'''

import time
import requests
from requests.exceptions import RequestException
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # 改变标准输出的默认编码


def get_page(url, refresh_times=3):
    try:
        response = requests.get(url)
        if (500 <= response.status_code < 600):
            if(refresh_times > 0):
                time.sleep(1)
                print('服务器出错，正在重试---')
                refresh_times -= 1
                get_page(url, refresh_times)
            return response.text
    except RequestException as e:
        print(e)
        return None


def run(url):
    get_page(url)


if __name__ == '__main__':
    #url = 'http://httpstat.us/500'
    url = 'http://www.google.com'
    run(url)
