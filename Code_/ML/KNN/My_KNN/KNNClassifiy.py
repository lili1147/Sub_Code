import numpy as np
from math import sqrt
from collections import Counter


class KNNClassifier:
    def __init__(self):
        self._x_train = None
        self._y_train = None

    def MyKnnClassifiy(self, x_train, y_train, x, k):
        assert x_train.shape[0] == y_train.shape[0], 'x must have same size as y'
        assert x_train.shape[1] == x.shape[0], 'the fetauers size must same'

        _x_train = x_train
        _y_train = y_train

        # distances = []
        # for item in _x_train:
        #   d = sqrt(np.sum((item-x)**2))
        #   distances.append(d)
        distances = [sqrt(np.sum((item - x)**2)) for item in _x_train]
        near_index = np.argsort(distances)
        topK_y = [y_train[i] for i in near_index[:k]]
        votess = Counter(topK_y)
        return votess.most_common(1)[0][0]
