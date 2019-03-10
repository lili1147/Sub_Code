'''
分析国家和数目的影响
'''

import numpy as np
import pandas as pd
import csv
import re

data = pd.read_csv('../../ks-projects-201612.csv', usecols=[11])

# print(data)
countries = {}

for item in range(0, len(data)):
    try:
        # print(data.loc[item].values)
        country = data.loc[item].values[0]
        if country in countries.keys():
            countries[country] += 1
        else:
            countries[country] = 1
    except:
        pass

print(countries)

{'GB': 27444, 'US': 256816, 'CA': 11962, 'NO': 524, 'AU': 6219, 'IT': 1741,
 'DE': 2666, 'IE': 575, 'ES': 1358, 'N,"0': 3785, 'MX': 212, 'SE': 1259,
 'FR': 1890, 'NL': 2252, 'NZ': 1132, 'CH': 470, 'AT': 374,
 'BE': 400, 'DK': 822, 'HK': 97, 'LU': 40, 'SG': 118}

GB  英国
US  美国
CA  加拿大
NO  挪威
AU  澳大利亚
IT  意大利
DE	德国
IE 	爱尔兰
ES  西班牙
MX  墨西哥
SE  瑞典
FR  法国
NL  荷兰
NZ  新西兰
CH  瑞士
AT  奥地利
BE  比利时
DK  丹麦
HK  中国香港
LU  卢森堡
SG  新加坡
