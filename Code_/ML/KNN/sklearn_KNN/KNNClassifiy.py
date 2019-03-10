# import numpy as np
# from math import sqrt
# from collections import Counter


# class KNNClassifier:
#     def __init__(self):
#         self._x_train = None
#         self._y_train = None
#         self._k = None

#     def MyKnnClassifiy(self, x_train, y_train, x, k):
#         assert x_train.shape[0] == y_train.shape[0], 'x must have same size as y'
#         assert x_train.shape[1] == x.shape[0], 'the fetauers size must same'

#         self._x_train = x_train
#         self._y_train = y_train
#         self._k = k

#         distances = []
#         for item in x_train:
#             d = sqrt(np.sum((item - x)**2))
#             distances.append(d)
#         # distances = [sqrt(np.sum((item - x)**2)) for item in _x_train]
#         near_index = np.argsort(distances)
#         topK_y = [y_train[i] for i in near_index[:k]]
#         votes = Counter(topK_y)
#         print(votes)
#         return votes.most_common(1)[0][0]


# x = [[1.23, 2.122], [2.3, 3.122], [3.6, 4.47], [3.22, 4.56]]
# y = [1, 0, 0, 0]
# x_train = np.array(x)
# y_train = np.array(y)
# x0 = [2.1, 3.2]
# x0 = np.array(x0)
# print(type(x0))
# print(x0.shape)
# my_knn = KNNClassifier()
# y_predict = my_knn.MyKnnClassifiy(x_train, y_train, x0, 3)
# print(y_predict)

import numpy as np
from math import sqrt
from collections import Counter


class KNNClassify:
    def __init__(self, k):
        self._x_train = None
        self._y_train = None
        self._k = k

    def fit(self, x_train, y_train):
        self._x_train = x_train
        self._y_train = y_train
        return self

    def predict(self, x_predict):
        y_predict = [self._predict(x) for x in x_predict]
        return np.array(y_predict)

    def _predict(self, x):
        #distances = [sqrt(np.sum((item - x)**2)) for item in self._x_train]
        distances = []
        for item in x_train:
            print(x)
            d = sqrt(np.sum((item - x)**2))
            distances.append(d)
        near_index = np.argsort(distances)
        mostK_y = [self._y_train[i] for i in near_index[:self._k]]
        votes = Counter(mostK_y)
        return votes.most_common(1)[0][0]


x = [[1.23, 2.122], [2.3, 3.122], [3.6, 4.47], [3.22, 4.56]]
y = [1, 0, 0, 0]
x_train = np.array(x)
y_train = np.array(y)
x0 = [[2.1, 3.2]]
x0 = np.array(x0)
my_knn = KNNClassify(3)
my_knn.fit(x_train, y_train)
y_predict = my_knn.predict(x0)
print(y_predict)
