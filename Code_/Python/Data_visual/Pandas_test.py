
'''对Pandas库的使用

1.数据质量分析：异常值和缺失值
（1）使用pandas 中的describe()函数就可以查看数据的基本情况
	其中mean位平均值 std为标准差 min最小值 max 最大值 25% 50% 75%的分位数
	读取 .csv 格式时,通过使用usecols 读取指定列
（2）



'''
# import pandas as pd
# import matplotlib.pyplot as plt
# content = 'data.csv'


# # 使用usecols 读取指定的列数信息
# data = pd.read_csv(content, usecols=[4])
# new_data = data.head()
# print(len(new_data))
# print(new_data)

# # 使用describe函数分析数值
# print(new_data.describe())


# # 使用箱线图进行数值质量分析
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# plt.figure()  # 建立图像
# p = new_data.boxplot(return_type='dict')  # 画出箱线图 ，直接使用DataFrame 的方法 返回p为字典状态
# x = p['fliers'][0].get_xdata()   # 'flies'即为异常值的标签
# y = p['fliers'][0].get_ydata()
# y.sort()  # 从小到大排序，该方法直接改变源对象

# # 使用annotata添加注释
# # 其中有些相近的点，注解会出现重叠，难以看清，需要一些技巧来控制
# # 以下参数都是经过调试的，需要具体问题具体调试
# for i in range(len(x)):
#     if i > 0:
#         plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
#         print('use')
#     else:
#         plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))
#         print('noues')

# plt.show()  # 展示箱线图


# 箱线图
import pandas as pd
import matplotlib.pyplot as plt
import csv

# 读取csv的第一种方法 通过cvs.reader(f) 返回一个文件的迭代器
content = 'data.csv'
# data = csv.reader(content)
# print(data)


# 使用pandas中的read_csv方法读取csv,返回文件内容
data = pd.read_csv(content, usecols=[4])
# print(data)
new_data = data.head()
print(data.head())

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.figure()
p = new_data.boxplot(return_type='dict')
plt.show()
