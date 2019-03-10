import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl


mpl.rcParams['font.sans-serif'] = ['SimHei']
data = pd.read_csv('data.csv')
# 打印前5条数据
print(data.head())

new_data = data[data['shot_made_flag'].notnull()]
# print(new_data)

plt.figure(figsize=(10, 20))
jumpshot = new_data[new_data['combined_shot_type'] == 'Jump Shot']
layup = new_data[new_data['combined_shot_type'] == 'Layup']
dunk = new_data[new_data['combined_shot_type'] == 'Dunk']
tipshot = new_data[new_data['combined_shot_type'] == 'Tip Shot']
hookshot = new_data[new_data['combined_shot_type'] == 'Hook Shot']
bankshot = new_data[new_data['combined_shot_type'] == 'Bank Shot']

plt.scatter(jumpshot.loc_x, jumpshot.loc_y, color='grey')
plt.scatter(layup.loc_x, layup.loc_y, color='red')
plt.scatter(dunk.loc_x, dunk.loc_y, color='yellow')
plt.scatter(tipshot.loc_x, tipshot.loc_y, color='green')
plt.scatter(hookshot.loc_x, hookshot.loc_y, color='black')
plt.scatter(bankshot.loc_x, bankshot.loc_y, color='blue')
label = ['跳投', '上篮', '扣篮', '补篮', '勾手', '擦板']
plt.legend(label, loc=7)
plt.title('投篮位置')

attack_method = new_data['combined_shot_type'].value_counts()
a = np.array([1, 2, 3, 4, 5, 6])
plt.bar(a, attack_method, align='center')
plt.xlabel('进攻方式')
plt.ylabel('进攻次数')
plt.title('科比进攻方式')
plt.grid(linestyle='--', linewidth=1)
plt.ylim(0, 800)
plt.xticks(a, ('跳投', '上篮', '扣篮', '补篮', '勾手', '擦板'))
plt.show()
