# import csv
# import numpy as np
# import pandas as pd
# import re
# data = pd.read_csv('../ks-projects-201612.csv', usecols=[5])


# dic = {}
# for item in np.arange(0, len(data)):
#     time = data.values[item][0]
#     # print(time)
#     try:
#         year = re.findall(r'(\d+)', time)
#         # print(year)
#         # print(item)
#         year1 = year[0]
#         # print(type(year[0]))
#         if int(year1) <2020:
#             if year1 in dic.keys():
#                 dic[year1] += 1
#                 print(year)
#                 print(item)
#             else:
#                 dic[year1] = 1
#     except IndexError:
#         pass
#     except TypeError:
#         pass

# print(dic)

# {'2015': 77122, '2013': 43942, '2012': 41393, '2016': 57626, '2014': 65907,
#  '2011': 24991, '2010': 9051, '2017': 1225, '2009': 899}


# 组合查询：现已将每个年份的的众筹项目数统计出来了  组合查询的目的是统基础每年各个类别的众筹项目。制作变化的图表

# 组合查询结果：
# 2009年：{'Music': 189, 'Film & Video': 207, 'Publishing': 88, 'Photography': 53, 'Technology': 42, 'Journalism': 30, 'Art': 125, 'Food': 22, 'Games': 33, 'Fashion': 21, 'Theater': 38, 'Comics': 16, 'Crafts': 7, 'Design': 23, 'Dance': 5}
# 2010年：{'Film & Video': 3108, 'Music': 2075, 'Art': 775, 'Photography': 384, 'Theater': 551, 'Journalism': 173, 'Technology': 202, 'Fashion': 139, 'Publishing': 622, 'Comics': 230, 'Food': 243, 'Games': 218, 'Design': 141, 'Dance': 137, 'Crafts': 53}
# 2011年：{'Music': 6323, 'Theater': 1421, 'Film & Video': 7859, 'Publishing': 2056, 'Technology': 420, 'Comics': 577, 'Photography': 880, 'Design': 767, 'Fashion': 557, 'Art': 2219, 'Dance': 399, 'Journalism': 170, 'Food': 539, 'Games': 693, 'Crafts': 111}
# 2012年：{'Music': 9036, 'Food': 1812, 'Photography': 1202, 'Film & Video': 9642, 'Fashion': 1601, 'Comics': 1141, 'Theater': 1804, 'Design': 1836, 'Games': 2661, 'Technology': 816, 'Publishing': 5288, 'Art': 3449, 'Journalism': 281, 'Dance': 522, 'Crafts': 302}
# 2013年：{'Film & Video': 9344, 'Publishing': 5695, 'Music': 6956, 'Fashion': 2312, 'Art': 3386, 'Photography': 1209, 'Games': 4038, 'Theater': 1475, 'Technology': 1689, 'Food': 2141, 'Design': 3080, 'Dance': 533, 'Comics': 1392, 'Crafts': 478, 'Journalism': 214}
# 2014年：{'Food': 6194, 'Design': 5251, 'Film & Video': 9947, 'Crafts': 1796, 'Comics': 1560, 'Theater': 1788, 'Music': 7454, 'Games': 5873, 'Fashion': 4190, 'Dance': 699, 'Art': 4960, 'Technology': 5924, 'Photography': 2300, 'Publishing': 7132, 'Journalism': 839}
# 2015年：{'Publishing': 7408, 'Film & Video': 10255, 'Design': 6605, 'Food': 6192, 'Art': 5327, 'Games': 7381, 'Music': 8550, 'Technology': 9689, 'Crafts': 2566, 'Fashion': 5200, 'Photography': 2242, 'Dance': 619, 'Comics': 1917, 'Theater': 1693, 'Journalism': 1477}
# 2016年：{'Food': 3896, 'Games': 6882, 'Crafts': 1816, 'Comics': 1866, 'Design': 5904, 'Art': 3589, 'Publishing': 5749, 'Film & Video': 7044, 'Fashion': 4198, 'Technology': 7036, 'Music': 5874, 'Photography': 1343, 'Theater': 1146, 'Dance': 435, 'Journalism': 848}
# 2017年1月{'Food': 80, 'Art': 75, 'Technology': 206, 'Theater': 21, 'Music': 160, 'Design': 132, 'Journalism': 25, 'Publishing': 113, 'Fashion': 74, 'Film & Video': 123, 'Crafts': 33, 'Games': 117, 'Comics': 28, 'Dance': 10, 'Photography': 28}

import numpy as np
import pandas as pd
import csv
import re

data = pd.read_csv('../ks-projects-201612.csv', usecols=[3, 5])
dic = {}
for item in np.arange(0, len(data)):
    type_time = data.loc[item].values
    # print(type_time)
    time = type_time[1]
    # year = re.findall(r'(\d+)', time)
    # print(year[0])
    try:
        year = re.findall(r'(\d+)', time)
        year1 = year[0]
        if int(year1) == 2017:
            if type_time[0] in dic.keys():
                dic[type_time[0]] += 1
            else:
                dic[type_time[0]] = 1
    except IndexError:
        pass
    except TypeError:
        pass
print(dic)
