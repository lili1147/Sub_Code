'''K-近邻算法
	
'''
from numpy import *
import operator
from collections import Counter


def createDataSet():
    groups = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return groups, labels


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
    print(votes.most_common(1)[0][0])


groups, labels = createDataSet()
Myknn([1, 1], groups, labels, 3)
