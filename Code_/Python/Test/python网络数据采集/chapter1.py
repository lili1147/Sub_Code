'''
正则表达式可以作为BeautifulSoup()语句的任意一个参数，让目标元素查找工作更为灵活


# example 1
from bs4 import BeautifulSoup
import requests
import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # 改变标准输出的默认编码


html = requests.get('http://www.pythonscraping.com/pages/page3.html')

soup = BeautifulSoup(html.text, 'lxml')
# 第一种正则表达式
# imges = soup.find_all('img', {'src': re.compile('.*?/img/gifts/img*?')})
# 第二种正则表达式
imges = soup.find_all('img', {'src': re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
# 正则与BeautifulSoup()的一起使用
for img in imges:
    print(img)



# example 2
# 获取百度百科的任何页面并提取所有链接
import requests
from bs4 import BeautifulSoup
import sys
import io
import re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # 改变标准输出的默认编码
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
response = requests.get('https://baike.baidu.com/', headers=headers)
content = response.text
# print(content)
soup = BeautifulSoup(content, 'lxml')
items = soup.find_all('a', {'href': re.compile('https\:\/\/.*?\.baidu\.com\/')})  # 用正则表达式匹配百科的内链接
for item in items:
    if 'href' in item.attrs:
        print(item.attrs['href'])html





# example 3
# 模拟随机点击百度百科的内链接以及子链接，直到没有可以点击的

import requests
import re
import datetime
import random
import sys
import io
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException as e:
        print(e)
        return None


def get_url(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all('a', {'href': re.compile('https\:\/\/.*?\.baidu\.com\/')})
    return urls


def run():
    print(datetime.datetime.now())
    random.seed(datetime.datetime.now())  # 所以如果想产生不同的随机数就需要用当前时间作为种子
    url = 'https://baike.baidu.com/'
    html = get_html(url)
    urls = get_url(html)
    while len(urls) > 0:
        new_url = urls[random.randint(0, len(urls) - 1)].attrs['href']
        print(new_url)
        html = get_html(new_url)
        print(html)
        urls = get_url(html)
        print('lili niubi')

    # print(random.randint(1, 20))
    # print(random.randint(1, 20))


if __name__ == '__main__':
    run()




from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from random import choice
import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def getInternalLinks(bsObj, includeUrl):
    return [eachlink.attrs['href'] for eachlink in bsObj.find_all("a", href=re.compile("^(/|.*" + includeUrl + ")")) if 'href' in eachlink.attrs]


def getExternalLinks(bsObj, excludeUrl):
    return [eachlink.attrs['href'] for eachlink in bsObj.find_all("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")) if 'href' in eachlink.attrs]


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


allINlinks = set()
allEXlinks = set()


def getAllexternalLinks(startPage):
    try:
        with urlopen(startPage) as html:
            bsObj = BeautifulSoup(html, "html.parser")
    except HTTPError as e:
        print(e)
    else:
        allinternallinks = getInternalLinks(bsObj, splitAddress(startPage)[0])
        allexternallinks = getExternalLinks(bsObj, splitAddress(startPage)[0])
        print("************external*******************************")
        for eachexternallink in allexternallinks:
            if eachexternallink not in allEXlinks:
                allEXlinks.add(eachexternallink)
                print(eachexternallink)
        print("************internal*******************************")
        for eachinternallink in allinternallinks:
            if eachinternallink not in allINlinks:
                allINlinks.add(eachinternallink)
                print(eachinternallink)
                getAllexternalLinks(eachinternallink)

if __name__ == "__main__":
    getAllexternalLinks("http://www.oreilly.com/")
# 别人的代码

'''


# example4 不限制连接的跳转
import requests
import re
import datetime
import random
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


random.seed(datetime.datetime.now())


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    try:
        response = requests.get('https://www.oreilly.com/', headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        print(e)
        return None

# 获取所有的内链接，内链接以'/'开头


def get_internal_urls(html):
    inter_urls = []
    soup = BeautifulSoup(html, 'lxml')
    # pattern = re.compile('')
    # urls = soup.find_all('a', {'href': re.compile()})
    urls = soup.find_all('a', href=re.compile('^\/+[A-Za-z0-9]'))
    # print(urls)
    for url in urls:
        inter_urls.append(url.attrs['href'])
    return inter_urls


# 获取外部链接
def get_external_urls(html):
    external_urls = []
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all('a', href=re.compile('\/\/www.*?'))
    for url in urls:
        if url.attrs['href'] is not None:
            if url.attrs['href'] not in external_urls:
                external_urls.append(url.attrs['href'])
    return external_urls


def splitAddress(address):
    addressParts = address.replace('http://', '')
    return addressParts


def run(url):
    html = get_html(url)
    external_urls = get_external_urls(html)
    # print(external_urls)
    if len(external_urls) == 0:
        interal_urls = get_internal_urls(html)
        html = get_html(interal_urls[random.randint(0, len(interal_urls) - 1)])
        if html is not None:
            external_urls = get_external_urls(html)
            if len(external_urls) == 0:
                print('没有外链接了')
                return None
            else:
                return external_urls[random.randint(0, len(external_urls) - 1)]
        else:
            print('文本为空')

    else:
        return external_urls[random.randint(0, len(external_urls) - 1)]


def main(url, times):

    print('程序正在执行')
    external_url = run(url)
    print('--------')
    print(external_url)
    if times > 0:
        main(external_url, times)
        times -= 1


main('https://www.oreilly.com/', 2)

# if __name__ == '__main__':
#     main()
