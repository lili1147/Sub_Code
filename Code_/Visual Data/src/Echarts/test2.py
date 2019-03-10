
'''

类型         成功次数 		 失败次数		取消次数	   正在直播次数	 挂起次数		未定义
Music        21717			  19153		      2932		 462		   126		     2227	
Publishing	 10236			  19869  		  3085		 448		   51			 462
Film & Video 21357			  29580			  5153	     498		   92 			 849
Food		 5227			  13557			  1930		 277		   128			  0
Design		 7920			  11966 	      3111		 544	       196			  2
Crafts		 1665 			  4617			  681		 141		   58			  0
Games		 9346			  12954	          4958		 460		   177			  1
Comics		 4491			  3398			  702		 117		   19			  0
Fashion		 4289 			  11438			  2126		 328		   108	  		  3
Theater		 5977			  3326			  547		 65			   21			  1
Art			 9633			  12059	 		 1885		 256		   72			  0
Technology	 5045			  16281			 3741		 621		   323			  3
Journalism	 886			  2651			  433		 59				48        	  0

'''

import csv
import numpy as np
import pandas as pd
data = pd.read_csv('../ks-projects-201612.csv', usecols=[3, 9])
# # print(data)
# num = 0
# for i in np.arange(0, len(data)):
#     if data.loc[i].values[0] == 'Music':
#         num += 1
# print(num)


# Film & Video的成功，失败，取消的数 21357  29580 5153
# data_film = data.loc[data['main_category '] == 'Film & Video']
# data_film_success = data_film.loc[data['state '] == 'successful']
# print(len(data_film_success))
# data_film_fail = data_film.loc[data['state '] == 'failed']
# print(len(data_film_fail))
# data_film_cancel = data_film.loc[data['state '] == 'canceled']
# print(len(data_film_cancel))


data_item = data.loc[data['main_category '] == 'Journalism']
# print(len(data_item))
data_item_success = data_item.loc[data['state '] == 'successful']
print(len(data_item_success))
data_item_failed = data_item.loc[data['state '] == 'failed']
print(len(data_item_failed))
data_item_cancel = data_item.loc[data['state '] == 'canceled']
print(len(data_item_cancel))
data_item_live = data_item.loc[data['state '] == 'live']
print(len(data_item_live))
data_item_sup = data_item.loc[data['state '] == 'suspended']
print(len(data_item_sup))
data_item_un = data_item.loc[data['state '] == 'undefined']
print(len(data_item_un))
