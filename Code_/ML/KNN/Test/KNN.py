'''
数据集的三个特征X：每年获得的飞行常客里程数
				玩视频游戏所耗时间百分比
				每周消费的冰淇凌公升数

			Y:1代表不喜欢，2代表魅力一般，3代表极具魅力
1.准备数据:从文本中解析数据
'''
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

from numpy import *
import operator
from collections import Counter


'''
函数说明：打开txt文件，对数据进行分类 1 代表didntLike   不喜欢
								   2 代表smallDoses  魅力一般
								   3 代表largeDoses  极具魅力

输入：filename
输出：返回Numpy可识别的数据类型，以及划分好的标签

读取文件时： read        读取整个文件
			readline    读取下一行
			readlines	读取整个文件到一个迭代器中(读取到list中，)

'''


def fileTomatrix(filename):
    # with open('datingTestSet.txt', 'r') as f:
    #     data = f.readlines()
    #     print(data)
    #     print(type(data))
    f = open(filename)
    # 读取文件内容
    data = f.readlines()
    # 获取内容的行数，用于初始化矩阵
    lne_data = len(data)
    # 初始化矩阵
    new_matrix = np.zeros((lne_data, 3))
    # 初始化向量标签
    classLabelVector = []
    index = 0
    for line in data:
        # 去除空白符
        line = line.strip()
        # 使用s.split('\t')将字符串进行切片 得到List
        line_list = line.split('\t')
        # 将line_list中的前三个放入到特征矩阵中
        new_matrix[index, :] = line_list[0:3]
        index += 1
        if line_list[-1] == 'largeDoses':
            classLabelVector.append(3)
        elif line_list[-1] == 'smallDoses':
            classLabelVector.append(2)
        elif line_list[-1] == 'didntLike':
            classLabelVector.append(1)
    # print(new_matrix)
    # print(len(classLabelVector))
    return new_matrix, classLabelVector


def showdatas(matrix, Label):
    # 设置格式
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['font.serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False  # 用控制中文乱码
    # print(matrix[:, 0])
    # 将画布分隔四个区域，asx[0][0]表示第一行第一个区域
    fig, axs = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False, figsize=(13, 8))
    numberOfLabels = len(Label)
    LabelColors = []
    for i in Label:
        if i == 1:
            LabelColors.append('black')
        elif i == 2:
            LabelColors.append('orange')
        elif i == 3:
            LabelColors.append('red')

    # 第一个散点图 矩阵的第一列 飞行里程  ，矩阵第二列 玩游戏的比例
    axs[0][0].scatter(x=matrix[:, 0], y=matrix[:, 1], color=LabelColors, s=30, alpha=.5)\
        # 设置标题和坐标轴
    axs0_title_text = axs[0][0].set_title('每年获得的飞行常客里程数与玩视频游戏所消耗的时间占比')
    asx0_xlabel_text = axs[0][0].set_xlabel('每年获得的飞行常客里程数')
    asx0_ylabel_text = axs[0][0].set_ylabel('视频游戏所消耗的时间占比')

    plt.setp(axs0_title_text, size=12, weight='bold', color='red')
    plt.setp(asx0_xlabel_text, size=9, weight='bold', color='black')
    plt.setp(asx0_ylabel_text, size=9, weight='bold', color='black')

    # 第二个散点图 每年的飞行里程数 和 每周消费的冰淇凌公升数
    axs[0][1].scatter(x=matrix[:, 0], y=matrix[:, 2], color=LabelColors, s=30, alpha=.5)
    axs1_title_text = axs[0][1].set_title('每年获得的飞行常客里程数与每周消费的冰淇凌公升数')
    asx1_xlabel_text = axs[0][1].set_xlabel('每年获得的飞行常客里程数')
    asx1_ylabel_text = axs[0][1].set_ylabel('每周消费的冰淇凌公升数')

    plt.setp(axs1_title_text, size=12, weight='bold', color='red')
    plt.setp(asx1_xlabel_text, size=9, weight='bold', color='black')
    plt.setp(asx1_ylabel_text, size=9, weight='bold', color='black')

    # 第三个散点图
    axs[1][0].scatter(x=matrix[:, 1], y=matrix[:, 2], color=LabelColors, s=30, alpha=.5)
    axs2_title_text = axs[1][0].set_title('视频游戏所消耗的时间占比与每周消费的冰淇凌公升数')
    asx2_xlabel_text = axs[1][0].set_xlabel('视频游戏所消耗的时间占比')
    asx2_ylabel_text = axs[1][0].set_ylabel('每周消费的冰淇凌公升数')

    plt.setp(axs2_title_text, size=12, weight='bold', color='red')
    plt.setp(asx2_xlabel_text, size=9, weight='bold', color='black')
    plt.setp(asx2_ylabel_text, size=9, weight='bold', color='black')

    # 设置图例
    didntLike = mlines.Line2D([], [], color='black', marker='.', markersize=6, label='didntLike')
    smallDoses = mlines.Line2D([], [], color='orange', marker='.', markersize=6, label='smallDoses')
    largeDoses = mlines.Line2D([], [], color='red', marker='.', markersize=6, label='largeDoses')
    # 添加图例
    axs[0][0].legend(handles=[didntLike, smallDoses, largeDoses], loc='upper right')
    axs[0][1].legend(handles=[didntLike, smallDoses, largeDoses], loc='upper right')
    axs[1][0].legend(handles=[didntLike, smallDoses, largeDoses], loc='upper right')

    plt.show()


def Myknn(myarray, DataSets, labels, k):
    distances = []
    for data in DataSets:
        distance = sqrt(sum((myarray - data)**2))
        distances.append(distance)
        # print(distance)
    # print(distances)
    near_index = argsort(distances)
    # print(near_index)
    # 根据排序的索引导出标签
    labels_index = [labels[i] for i in near_index[:k]]
    # print(labels_index)
    # 选出最多的那一个标签
    votes = Counter(labels_index)
    # print(votes) 返回的是字典Counter({'A': 2, 'B': 1})
    return votes.most_common(1)[0][0]
    # print(votes.most_common(1)[0][0])


'''
数据归一化：在计算数字值差值最大的属性对计算结果影响最大，飞行里程数远大于其他特征值

'''


def autoNormal(dataset):
    minval = dataset.min(0)  # 参数0使得函数可以从列中选出最小值，而不是选取当前行的最小值
    maxval = dataset.max(0)
    ranges = maxval - minval
    normalData = zeros(shape(dataset))
    m = dataset.shape[0]
    normalData = dataset - tile(minval, (m, 1))
    normalData = normalData / tile(ranges, (m, 1))
    return normalData, minval, maxval


'''
测试，对knn算法进行测试
'''


def TestKnn(DataSets, Labels):
    num = 0
    index = 0
    # normaldata, minval, maxval = autoNormal(DataSets)
    for data in DataSets:
        lichengshu = data[0]
        game = data[1]
        ice_cream = data[2]
        myarray = np.array([lichengshu, game, ice_cream])
        pre_knn = Myknn(myarray, DataSets, Labels, 3)
        if pre_knn == Labels[index]:
            num += 1
        index += 1
    print('KNN算法的准确率为', 100 * (num / 1000), '%')


if __name__ == '__main__':
    new_matrix, Label = fileTomatrix('datingTestSet.txt')
    # print(new_matrix)
    # print(Label[:20])
    # showdatas(new_matrix, Label)

    Person = ['不喜欢', '一般喜欢', '非常喜欢']
    # lichengshu = float(input('里程数'))
    # game = float(input('游戏占比'))
    # ice_cream = float(input('冰淇凌公升数'))

    # 测试KNN的准确率
    TestKnn(new_matrix, Label)

    # # 生成测试数据
    # myarray = np.array([80000, 12, 0.5])
    # result = Myknn(myarray, new_matrix, Label, 3)
    # print(Person[result - 1])
