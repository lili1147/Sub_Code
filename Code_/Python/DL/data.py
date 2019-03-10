'''
查看imdb中电影评论的数据集
'''

from keras.datasets import imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(
    path='C:/Users/lili/.keras/datasets/imdb.npz', num_words=10000
)

# print(type(train_data))
# for data in train_data[:2]:
#     print(data)
#     print(type(data))
# word_index = imdb.get_word_index(path='C:/Users/lili/.keras/datasets/imdb_word_index.json')
# print(type(word_index))
# for key, value in word_index.items():
#     print(key, value)
# word = word_index.get(1, None)
# print(word)

# # 键值颠倒  使用列表生成器
# reverse_dict = dict(
#     [(value, key) for (key, value) in word_index.items()]
# )

# for key, value in reverse_dict.items():
#     print(key, value)
# word = reverse_dict.get(194, 'none')
# print(word)


print(train_data)

# import numpy as np


# def vectorize_sequences(sequences, dimension=10000):
#     results = np.zeros((len(sequences), dimension))
#     for i, sequence in enumerate(sequences):
#         results[i, sequence] = 1
#     return results


# # print(len(train_data[0]))
# x_train = vectorize_sequences(train_data)
# # print(x_train)
# # print(len(x_train))
# print(x_train.shape)
