import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from collections import Counter

iris_data = datasets.load_iris()

# 为可视化方便，只取两维特征
x = iris_data.data[:, 2:]

y = iris_data.target


# plt.scatter(x[y == 0, 0], x[y == 0, 1])
# plt.scatter(x[y == 1, 0], x[y == 1, 1])
# plt.scatter(x[y == 2, 0], x[y == 2, 1])
# plt.show()

# 决定在哪个维度，哪个之值上进行划分

def split(x, y, d, value):
    index_l = (x[:, d] <= value)
    index_r = (x[:, d] > value)
    return x[index_l], x[index_r], y[index_l], y[index_r]


def entropy(y):
    counters = Counter(y)
    res = 0.0
    for i in counters.values():
        p = i / len(y)
        res += -p * np.log(p)
    return res


def try_split(x, y):
    best_entropy = float('inf')
    best_d, best_v = -1, -1
    for d in range(x.shape[1]):
        sort_index = np.argsort(x[:, d])
        # print(sort_index)
        for i in range(1, len(x)):
            if (x[sort_index[i - 1], d]) != (x[sort_index[i], d]):
                v = (x[sort_index[i - 1], d] + x[sort_index[i], d]) / 2
                x_l, x_r, y_l, y_r = split(x, y, d, v)
                e = entropy(y_l) + entropy(y_r)
                if e < best_entropy:
                    best_entropy = e
                    best_d = d
                    best_v = v
    return best_entropy, best_d, best_v
`

# def try_split(x, y):
#     # 初始化参数
#     best_entropy = float('inf')
#     best_d, best_v = -1, -1
#     for d in range(x.shape[1]):
#         sort_index = np.argsort(x[:, d])
#         for i in range(1, len(x)):  # 不从0开始是为要和0比较i-1
#             if x[sort_index[i - 1], d] != x[sort_index[i], d]:
#                 v = (x[sort_index[i - 1], d] + x[sort_index[i], d]) / 2
#                 x_l, x_r, y_l, y_r = split(x, y, d, v)
#                 e = entropy(y_r) + entropy(y_l)
#                 if e < best_entropy:
#                     best_entropy = e
#                     best_d = d
#                     best_v = v
#     return best_entropy, best_d, best_v


e1, d1, v1 = try_split(x, y)
print('the best entropy is %f' % e1)
print('the best d is %d' % d1)
print('the best e is %f' % v1)


# 在进行第二维度的划分
x1_l, x1_r, y1_l, y1_r = split(x, y, d1, v1)

print('------')
print(entropy(y1_l))
print('------')
e2, d2, v2 = try_split(x1_r, y1_r)
print('the best entropy is %f' % e2)
print('the best d is %d' % d2)
print('the best e is %f' % v2)
