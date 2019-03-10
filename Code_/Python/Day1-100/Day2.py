'''
name = ['dj', 'lil', 'hd']


def func(i):
    return i + 10


def func2(str):
    return str + 'niubi'


name = list(map(func2, name))
print(name)


from bs4 import BeautifulSoup
import re


def splitAddress(address):
    addressParts = address.replace('http://', '')
    return addressParts


def get_external_urls(html):
    external_urls = []
    soup = BeautifulSoup('html', 'lxml')
    urls = soup.find_all('a', {'href': re.compile('.*?\/\/.*?')})
    print(urls)


def run():
    address = 'https://www.oreilly.com/'
    # urls = splitAddress(address)
    # print(urls)
    get_external_urls(address)


if __name__ == '__main__':
    run()





# 最大公约数和最小公倍数
def func():
    a = int(input('please input number:'))
    b = int(input('please input number:'))
    print(type(a))
    print(type(b))
    while(a % b != 0):
        temp = a % b
        a = b
        b = temp
    return b


if __name__ == '__main__':
    print(func())

# 递归实现

# def gcd(a, b):
#     if b:
#         return gcd(b, a % b)
#     else:
#         return a


# if __name__ == '__main__':
#     a = int(input('num1:'))
#     b = int(input('num2'))
#     print(gcd(a, b))


'''


# old_dict = {
#     '1': 'lili',
#     '2': 'dj',
#     '3': 'admin'
# }

# # zaifor前面的叫列表生成式 ，
# new_dict = ([(value, key) for key, value in old_dict.items()])
# print(type(new_dict))
# print(new_dict)


# import numpy as np

# results = np.zeros((2, 3))
# for i, sequence in results:
#     print(i)

# name = ['lili', 'dj', 'hah']
# for i in enumerate(name):
#     print(i)

# num = [[3, 6, 9], [2, 4, 8]]
# results = np.zeros((len(num), 10))
# for i in results:
#     print(i)
# print('-------')

# for i, sequence in enumerate(num):
#     print(i, sequence)
#     results[i, sequence] = 1
# for i in results:
#     print(i)
# print(results)


# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# -------
# 0 [3, 6, 9]
# 1 [2, 4, 8]
# [0. 0. 0. 1. 0. 0. 1. 0. 0. 1.]
# [0. 0. 1. 0. 1. 0. 0. 0. 1. 0.]


# results = range(1, 10)
# print(type(results))
# for i in results:
#     print(i)


# import os
# os.environ['CUDA_VISIBLE_DEVICES'] = "1"  # 使用第几个GPU， 0是第一个
# import tensorflow as tf
# import numpy as np
# hello = tf.constant('hhh')
# sess = tf.Session()
# print(sess.run(hello))


# import tensorflow as tf

# sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))


# import tensorflow as tf

# tf.device('/gpu:2')

# a = tf.constant([1.0, 2.0, 3.0], shape=[3], name='a')
# b = tf.constant([1.0, 2.0, 3.0], shape=[3], name='b')
# c = a + b
# # 通过log_device_placement参数来输出运行每一个运算的设备。
# sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# print(sess.run(c))


# import tensorflow as tf
# a = tf.constant([1.,2.,3.,4.,5.,6.], shape=[2,3], name='a')
# b = tf.constant([1.,2.,3.,4.,5.,6.], shape=[3,2], name='b')
# c = tf.matmul(a,b)
# with tf.Session(config= tf.ConfigProto(log_device_placement=True)) as sess:
#     print(sess.run(c))


# import tensorflow as tf
# sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))


# from tensorflow.python.client import device_lib
# print(device_lib.list_local_devices())


# import matplotlib.pyplot as plt

# x = (1, 2, 3, 4, 5)
# y = (1, 2, 3, 4, 5)

# plt.plot(x, y, 'b', label='line')
# plt.legend()
# plt.show()


# import tensorflow as tf
# a = tf.constant([1.0, 2.0, 3.0], name='input1')
# b = tf.Variable(tf.random_uniform([3]), name='input2')
# add = tf.add_n([a, b], name='addOP')
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     writer = tf.summary.FileWriter("E://subline3/Code_/Python/Day1-100/", sess.graph)
#     print(sess.run(add))
# writer.close


# -*- coding: utf-8 -*-


# import tensorflow as tf


# # 将输入定义放入各自的命名空间中，从而使得TensorBoard可以根据命名空间来整理可视化效果图上的节点。

# with tf.name_scope("namespace_1"):

#     inputl = tf.constant([1.0, 2.0, 3.0], name="input1")


# with tf.name_scope("namespace_2"):

#     input2 = tf.Variable(tf.random_uniform([3]), name="input2")


# output = tf.add_n([inputl, input2], name="add")


# # 将当前的TensorFlow计算图写入日志

# writer = tf.summary.FileWriter("E://subline3/Code_/Python/Day1-100/logfile/",

#                                tf.get_default_graph())

# writer.close()


# -*- coding: utf-8 -*-

import keras

from keras.models import Sequential

from keras.layers import Dense

import numpy as np

import matplotlib.pyplot as plt

import time

# 输入训练数据 keras接收numpy数组类型的数据

x = np.array([[0, 1, 0],

              [0, 0, 1],

              [1, 3, 2],

              [3, 2, 1]])

y = np.array([0, 0, 1, 1]).T

# 最简单的序贯模型，序贯模型是多个网络层的线性堆叠

simple_model = Sequential()

# dense层为全连接层

# 第一层隐含层为全连接层 5个神经元 输入数据的维度为3

simple_model.add(Dense(5, input_dim=3, activation='relu'))

# 第二个隐含层 4个神经元

simple_model.add(Dense(4, activation='relu'))

# 输出层为1个神经元

simple_model.add(Dense(1, activation='sigmoid'))

# 编译模型,训练模型之前需要编译模型

# 编译模型的三个参数：优化器、损失函数、指标列表

simple_model.compile(optimizer='sgd', loss='mean_squared_error', metrics=['accuracy'])


class LossHistory(keras.callbacks.Callback):

    # 函数开始时创建盛放loss与acc的容器

    def on_train_begin(self, logs={}):

        self.losses = {'batch': [], 'epoch': []}

        self.accuracy = {'batch': [], 'epoch': []}

        self.val_loss = {'batch': [], 'epoch': []}

        self.val_acc = {'batch': [], 'epoch': []}

    # 按照batch来进行追加数据

    def on_batch_end(self, batch, logs={}):

        # 每一个batch完成后向容器里面追加loss，acc

        self.losses['batch'].append(logs.get('loss'))

        self.accuracy['batch'].append(logs.get('acc'))

        self.val_loss['batch'].append(logs.get('val_loss'))

        self.val_acc['batch'].append(logs.get('val_acc'))

        # 每五秒按照当前容器里的值来绘图

        if int(time.time()) % 5 == 0:

            self.draw_p(self.losses['batch'], 'loss', 'train_batch')

            self.draw_p(self.accuracy['batch'], 'acc', 'train_batch')

            self.draw_p(self.val_loss['batch'], 'loss', 'val_batch')

            self.draw_p(self.val_acc['batch'], 'acc', 'val_batch')

    def on_epoch_end(self, batch, logs={}):

        # 每一个epoch完成后向容器里面追加loss，acc

        self.losses['epoch'].append(logs.get('loss'))

        self.accuracy['epoch'].append(logs.get('acc'))

        self.val_loss['epoch'].append(logs.get('val_loss'))

        self.val_acc['epoch'].append(logs.get('val_acc'))

        # 每五秒按照当前容器里的值来绘图

        if int(time.time()) % 5 == 0:

            self.draw_p(self.losses['epoch'], 'loss', 'train_epoch')

            self.draw_p(self.accuracy['epoch'], 'acc', 'train_epoch')

            self.draw_p(self.val_loss['epoch'], 'loss', 'val_epoch')

            self.draw_p(self.val_acc['epoch'], 'acc', 'val_epoch')

    # 绘图，这里把每一种曲线都单独绘图，若想把各种曲线绘制在一张图上的话可修改此方法

    def draw_p(self, lists, label, type):

        plt.figure()

        plt.plot(range(len(lists)), lists, 'r', label=label)

        plt.ylabel(label)

        plt.xlabel(type)

        plt.legend(loc="upper right")

        plt.savefig(type + '_' + label + '.jpg')

    # 由于这里的绘图设置的是5s绘制一次，当训练结束后得到的图可能不是一个完整的训练过程（最后一次绘图结束，有训练了0-5秒的时间）

    # 所以这里的方法会在整个训练结束以后调用

    def end_draw(self):

        self.draw_p(self.losses['batch'], 'loss', 'train_batch')

        self.draw_p(self.accuracy['batch'], 'acc', 'train_batch')

        self.draw_p(self.val_loss['batch'], 'loss', 'val_batch')

        self.draw_p(self.val_acc['batch'], 'acc', 'val_batch')

        self.draw_p(self.losses['epoch'], 'loss', 'train_epoch')

        self.draw_p(self.accuracy['epoch'], 'acc', 'train_epoch')

        self.draw_p(self.val_loss['epoch'], 'loss', 'val_epoch')

        self.draw_p(self.val_acc['epoch'], 'acc', 'val_epoch')


logs_loss = LossHistory()


# 训练网络 2000次

# Keras以Numpy数组作为输入数据和标签的数据类型。训练模型一般使用fit函数

simple_model.fit(x, y, epochs=20000, callbacks=[logs_loss])

# 应用模型 进行预测

y_ = simple_model.predict_classes(x[0:1])

print("[0,1,0]的分类结果：" + str(y[0]))


logs_loss.end_draw()
