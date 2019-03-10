__author__ = 'lili'
__date__ = '2018/11/4 23:28'
'''
使用Beautiful 解析源码
使用正则发现行不通
使用selenium 打开目标网站，获得page_sourse
通过使用lxml解析 
找到统一table 资源
定位到tr for tr in trs[1:14]:
        rating = tr.find_all('td')[0].get_text()
        ratings.append(rating)
        使用pandas DataFrame()
        to_csv('data.csv',mode='a',encoding='utf-8_sig') 保存到csv文件
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import io
import re
import pandas as pd
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # 改变标准输出的默认编码


def get_page_html(url):
    driver = webdriver.Chrome()
    driver.get('http://www.mooctest.org/#/ProFinal')
    html = driver.page_source
    return html


def parse_page(html):
    soup = BeautifulSoup(html, 'lxml')
    member_list = soup.find_all('table', {'class': 'certificate-table'})
    # 个人移动
    mobie_list_personal = member_list[1]
    personal_trs = mobie_list_personal.find_all('tr')
    # 团体移动
    mobie_list_team = member_list[3]

    trs = mobie_list_team.find_all('tr')
    return trs, personal_trs


def save_as_list(trs):
    ratings = []
    teams = []
    universities = []
    provinces = []
    rewards = []
    booles = []
    teachers = []
    length = len(trs)
    for tr in trs[1:length]:
        rating = tr.find_all('td')[0].get_text()
        ratings.append(rating)

        team = tr.find_all('td')[1].get_text()
        teams.append(team)

        university = tr.find_all('td')[2].get_text()
        universities.append(university)

        province = tr.find_all('td')[3].get_text()
        provinces.append(province)

        reward = tr.find_all('td')[4].get_text()
        rewards.append(reward)

        boole = tr.find_all('td')[5].get_text()
        booles.append(boole)

        teacher = tr.find_all('td')[6].get_text()
        teachers.append(teacher)

    return ratings, teams, universities, provinces, rewards, booles, teachers
    #print(rating, team, university, province, reward, boole, teacher)


def save_as_csv(ratings, teams, universities, provinces, rewards, bools, teachers):
    data = pd.DataFrame()
    data['排名'] = ratings
    data['团队'] = teams
    data['学校'] = universities
    data['省份'] = provinces
    data['奖项'] = rewards
    data['是否晋级'] = bools
    data['指导教师'] = teachers

    data.to_csv('data.csv', mode='a', encoding='utf-8_sig', index=None)


def main():
    url = 'http://www.mooctest.org/#/ProFinal'
    html = get_page_html(url)
    # print(html)
    trs, personl_trs = parse_page(html)
    ratings, teams, universities, provinces, rewards, booles, teachers = save_as_list(trs)
    save_as_csv(ratings, teams, universities, provinces, rewards, booles, teachers)
    ratings, teams, universities, provinces, rewards, booles, teachers = save_as_list(personl_trs)
    save_as_csv(ratings, teams, universities, provinces, rewards, booles, teachers)


if __name__ == '__main__':
    main()
