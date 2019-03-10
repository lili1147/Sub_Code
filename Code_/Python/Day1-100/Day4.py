'''新闻多分类问题
要划分许多类别 所以称为多分类问题。
每个数据点只能划分到一个类别  称为单标签 多分类

每个数据点可以划分到多个类别   称为多标签 多分类



数据集：路透社数据集  也是keras内置的一部分

'''
from keras.datasets import reuters
(train_data, train_labels), (test_data, test_labels) = reuters.load_data(
    path='C:/Users/lili/.keras/datasets/reuters.npz', num_words=10000)

# 数据结构的了解

print(type(train_data))  # numpy 类型的数组
# for item in train_data:
#     print(item)
print(len(train_data))  # 训练集8982
print(len(test_data))  # 测试集2246
print(train_data.shape)  # （8982,）
print(len(train_labels))
print(type(train_labels))
# for item in train_labels:
#     print(item)
# 将索引解析为文本
word_index = reuters.get_word_index(path='C:/Users/lili/.keras/datasets/reuters_word_index.json')
print(type(word_index))  # 字典类型
# for key,value in word_index.items():
#     print(key, value)    #key是单词 value 是索引

new_word_index = dict([(value, key) for (key, value) in word_index.items()])
# for key, value in new_word_index.items():
#     print(key, value)  # key是索引 value 是单词


# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
def decode_news(text):
    return ' '.join((new_word_index.get(i - 3, '?') for i in text))


# print(decode_news(train_data[1]))

# 编码数据

import numpy as np


def vector_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1
    return results


x_train = vector_sequences(train_data)
x_test = vector_sequences(test_data)


# 将标签向量化
def one_hot_labels(labels, dimension=46):
    results = np.zeros((len(labels), dimension))
    for i, label in enumerate(labels):
        results[i, label] = 1
    return results


# 将标签向量化
y_train = one_hot_labels(train_labels)
# print(y_train)
y_test = one_hot_labels(test_labels)


# 构架网络
from keras import models
from keras import layers

# model = models.Sequential()
# model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
# model.add(layers.Dense(64, activation='relu'))
# model.add(layers.Dense(46, activation='softmax'))

# model.compile(optimizer='rmsprop',
#               loss='categorical_crossentropy',
#               metrics=['accuracy']
#               )

# x_val = x_train[:1000]
# partial_x_train = x_train[1000:]

# y_val = y_train[:1000]
# partial_y_train = y_train[1000:]

# history = model.fit(
#     partial_x_train,
#     partial_y_train,
#     epochs=20,
#     batch_size=512,
#     validation_data=(x_val, y_val)
# )


# # 绘制曲线
# import matplotlib.pylab as plt
# from pylab import mpl

# loss = history.history['loss']
# val_loss = history.history['val_loss']
# mpl.rcParams['font.sans-serif'] = ['SimHei']

# epochs = range(1, len(loss) + 1)

# plt.plot(epochs, loss, 'bo', label='training_loss')
# plt.plot(epochs, val_loss, 'b', label='validation_loss')
# plt.title('训练所失和验证损失')
# plt.xlabel('轮数')
# plt.ylabel('损失值')

# plt.legend()
# plt.show()


# 判断拟合情况后，重新选择迭代轮数
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(46, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(partial_x_train, partial_y_train, epochs=9, batch_size=512, validation_data=(x_val, y_val))
results = model.evaluate(x_test, y_test)
print(self.model.metrics_names)
print(results)
