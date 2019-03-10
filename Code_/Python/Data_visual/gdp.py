import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import numpy as np

import pandas as pd
filename = 'gdp.xlsx'
data = pd.read_excel(filename, index_col='日期')

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 定义使其正常显示中文字体黑体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示表示负号
plt.plot(data, label='重庆地区生产总值')
plt.legend()
plt.show()


# # 画出相关图
# from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
# # plot_acf(data)
# # plt.show()


# 平稳性检测
from statsmodels.tsa.stattools import adfuller
print('原始序列的检验结果为：', adfuller(data['地区总产值']))
# 原始序列的检验结果为： (0.0, 0.958532086060056, 9,
#		10, {'1%': -4.331573, '5%': -3.23295, '10%': -2.7487}, -474.6544401781462)
# 返回值依次为：adf, pvalue p值， usedlag, nobs, critical values临界值 , icbest, regresults, resstore
# adf 分别大于3中不同检验水平的3个临界值，单位检测统计量对应的p 值显著大于 0.05 ， 说明序列可以判定为 非平稳序列


# D_data = data.diff().dropna()
# D_data.columns = [u'产值差分']

# print(D_data)


# D_data.plot()  # 画出差分后的时序图
# plt.show()

# plot_acf(D_data)  # 画出自相关图
# plt.show()
# plot_pacf(D_data)  # 画出偏相关图
# plt.show()
# print(u'差分序列的ADF 检验结果为： ', adfuller(D_data['产值差分']))  # 平稳性检验
Data = data

# fig = plt.figure(figsize=(12, 8))
# ax1 = fig.add_subplot(111)
# data = np.log(Data)
# print(data)
# diff1 = data.diff(1).dropna()
# diff1.columns = [u'一次产值差分']
# diff1.plot(ax=ax1)
# plt.legend()
# plt.show()
# print(u'一次差分序列的ADF 检验结果为： ', adfuller(diff1['一次产值差分']))  # 平稳性检验


fig = plt.figure(figsize=(12, 8))
ax2 = fig.add_subplot(111)
data = np.log(Data)
diff2 = data.diff(3).dropna()
diff2.columns = [u'产值差分']
diff2.plot(ax=ax2)
plt.legend()
plt.show()
print(u'二次差分序列的ADF 检验结果为： ', adfuller(diff2['产值差分']))  # 平稳性检验

# 随机性检验(白噪声检验)
from statsmodels.stats.diagnostic import acorr_ljungbox
# print(acorr_ljungbox(data, lags=1))


# 找到合适的p(pacf),q(acf)
# 检查平稳时间序列的自相关图和偏相关图

from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
plot_acf(data)
plot_pacf(data)
plt.show()
