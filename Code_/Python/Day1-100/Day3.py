'''
for i in range(0, 32):
    print(i)
    # 输出i为0~31


import numpy as np

# 广播
x = np.random.random((64, 3, 32, 10))
y = np.random.random((32, 10))

z = np.maximum(x, y)  #两个形状不一样的向量，会进行广播
print(z.shape)
print(z)

'''


# 电影评论问题：二分类问题
import sys
import io
import numpy as np
# sys.stdout = io.TextIOWrapper(sys.stdout, encoding='utf-8')
from keras.datasets import imdb
from keras import models
from keras import layers
from keras import optimizers
from keras import metrics
import matplotlib.pyplot as plt


(train_data, train_labels), (test_data, test_labels) = imdb.load_data(
    path='C:/Users/lili/.keras/datasets/imdb.npz', num_words=10000)

print(train_data.shape)
# print('-----------')
# print(train_data[0])
# print(train_labels.shape)
# print('----------')
# print(train_labels[24999])


# word_index = imdb.get_word_index(path='C:/Users/lili/.keras/datasets/imdb_word_index.json')  # 将单词映射为整数索引的字典
# # print(type(word_index))  字典类型
# # for key, value in word_index.items():
# #     print(key, value)
# reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])


# # 字典的get方法 Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
# def decodeed_review(text):
#     # return ' '.join([reverse_word_index.get(i - 3, '?') for i in text])
#     return ' '.join([reverse_word_index.get(11, '?')])


# review = decodeed_review(train_data[0])
# print(review)


# 将整数序列编码为二进制矩阵
def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1
    return results


x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')


# 模型定义
model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))


# 编译模型
model.compile(optimizer=optimizers.RMSprop(lr=0.001), loss='binary_crossentropy', metrics=[metrics.binary_accuracy])


x_val = x_train[:10000]
partial_x_train = x_train[10000:]

y_val = y_train[:10000]
partial_y_train = y_train[10000:]


history = model.fit(
    partial_x_train,
    partial_y_train,
    epochs=20,
    batch_size=512,
    validation_data=(x_val, y_val)
)

history_dict = history.history
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']

epochs = range(1, len(loss_values) + 1)

plt.plot(epochs, loss_values, 'bo', label='Training loss')
plt.plot(epochs, val_loss_values, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
