'''
遵循robots.txt
动态UA
代理ip
'''

# from fake_useragent import UserAgent

# # ua = UserAgent()
# # print(ua.chrome)
# # print(ua.ie)
# # print(ua.random)

# import requests

# proxies = {
#     'https': '180.113.98.176',
#     'https': '116.192.175.93'
# }
# url = 'http://example.org'
# response = requests.get(url, proxies=proxies)
# print(response)


# 综合运用
# import re
# import time
# import chardet
# import requests
# import urllib.robotparser
# from fake_useragent import UserAgent

# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# # 获取headers


# def get_headers():
#     ua = UserAgent()
#     user_agent = ua.random
#     headers = {'User-agent': user_agent}
#     return headers


# # 获取代理ip。可以去爬免费代理，或者自己建一个代理池
# def get_proxies():
#     proxies = {
#         'http': '140.143.25.131',
#         # 'http': '61.135.217.7',
#         # 'http': '61.138.33.20'
#     }
#     return proxies


# # robots.txt检测
# def robot_text(robotstxt_url, headers, url):
#     rp = urllib.robotparser.RobotFileParser()
#     rp.set_url(robotstxt_url)
#     rp.read()
#     result = rp.can_fetch(headers['User-Agent'], url)
#     return result


# # 获取网页数据，这里没有返回data.text,
# # 因为抓取图片时返回为data.content
# def get_data(url, num_retries=3, proxies=None):
#     try:
#         data = requests.get(url, timeout=5, headers=headers)
#         print(data.status_code)
#     except requests.exceptions.ConnectionError as e:
#         print('请求错误', url)
#         print('错误详情:', e)
#         print('------')
#         data = None

#     if (data != None) and (500 <= data.status_code < 600):
#         if(num_retries > 0):
#             print('正在重试')
#             time.sleep(1)
#             num_retries -= 1
#             get_data(url, num_retries, proxies=proxies)
#     return data

# # 对网页进行解析


# def parse_data(data):
#     if data == None:
#         return None

#     charset = chardet.detect(data.content)
#     print(charset)
#     data.encoding = charset['encoding']
#     html_text = data.text
#     print(html_text)

#     title = re.findall('<title>(.*?)</title>', html_text)
#     return title


# if __name__ == '__main__':
#     headers = get_headers()
#     proxies = get_proxies()
#     data = get_data('http://wwww.baidu.com', num_retries=3, proxies=proxies)
#     title = parse_data(data)
#     print(title)
