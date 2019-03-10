'''
使用K-近邻算法分类器 对手写数字进行识别 0-9
	数据存储在文本文件中

	1.准备数据：首先观察数据，有两个txt, 为trainingDigits和testDigits。将图像格式处理为一个向量。
			   我们将把一个32x32的二进制图像矩阵转换成1x1024的向量
'''

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
from os import listdir
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier


'''
	img2vector(filename):该函数创建一个1x1024的numpy数组，然后打开指定文件，循环读出文件的前32行，
						 并将每行的头32个字符保存到数组中
'''


def myknn(my_array, train_matrix, labels, k):
    distances = []
    for data in train_matrix:
        distance = np.sqrt(np.sum((my_array - data)**2))
        distances.append(distance)
    near_index = np.argsort(distances)
    labels_index = [labels[i] for i in near_index[:k]]
    votes = Counter(labels_index)
    return votes.most_common(1)[0][0]
# print(votes) 返回的是字典Counter({'A': 2, 'B': 1})


def img2vector2(filename):
    my_array = np.zeros((1, 1024))  # 到底是存储在向量中还是矩阵中
    # print(my_array)
    f = open(filename)
    data = f.readlines()
    index = 0
    for line in data:
        # print(line)			# 00000000000001111000000000000000  其中每一行也是一个迭代器
        # print(type(line))  	# 类型 字符串类型
        for j in range(32):
            my_array[0, index] = int(line[j])
            index += 1
    # print(my_array[:64])
    # print(my_array.shape)
    return my_array


def img2vector(filename):
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        linestr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(linestr[j])
    return returnVect


'''
将数据输入到分类器中，检测分类的执行结果
'''


def handwritingClassTest():
    # 获取目录列表
    trainFileList = listdir('digits/trainingDigits/')
    m = len(trainFileList)
    trainMatrix = np.zeros((m, 1024))
    num_labels = []
    knn = KNeighborsClassifier()
    for i in range(m):
        filename = trainFileList[i]
        file = filename.split('.')[0]
        num_class = file.split('_')[0]
        # print(num_class)
        num_labels.append(num_class)
        trainMatrix[i, :] = img2vector('digits/trainingDigits/%s' % filename)

    # print(num_labels)
    # knn.fit(trainMatrix, num_labels)
    testFileList = listdir('digits/testDigits/')
    err_count = 0.0
    mtest = len(testFileList)
    for i in range(mtest):
        filename = testFileList[i]
        file = filename.split('.')[0]
        num_class = file.split('_')[0]
        testMatrix = img2vector('digits/testDigits/%s' % filename)
        # print(testMatrix)
        class_predict = myknn(testMatrix, trainMatrix, num_labels, 3)
        print('the classifier predict is %s, and the real class is %s' % (class_predict, num_class))
        if class_predict != num_class:
            err_count += 1

    print('一共错了%d个' % err_count)
    print('错误率为: %f' % (err_count / mtest))


# vector = img2vector('digits/trainingDigits/1_132.txt')
# print(vector[0, 0:64])
handwritingClassTest()
