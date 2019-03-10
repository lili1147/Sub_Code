from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = datasets.load_boston()

x = data.data

y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=666)

# line_model = LinearRegression()

# line_model.fit(x_train, y_train)

# score = line_model.score(x_test, y_test)
# print(score)


#  使用KNN回归 使用网格搜索最佳参数
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.model_selection import GridSearchCV


# knn_reg = KNeighborsRegressor()
# # print(knn_reg.fit(x_train, y_train))
# # print(knn_reg.score(x_test, y_test)) 0.48824123796594976
# param_grid = [
#     {
#         'weights': ['uniform'],
#         'n_eighbors':[i for i in range(1, 11)]
#     },
#     {
#         'weights': ['distance'],
#         'n_neighbors':[i for i in range(1, 11)],
#         'p':[i for i in range(1, 6)]
#     }
# ]
# grid_search = GridSearchCV(knn_reg, param_grid, n_jobs=-1, verbose=2)

# grid_search .best_score_


# 使用sklearn 中的随机梯度下降SGD
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler


# def train_test_split(x, y, test_ratio):
#     shuffle_indexs = np.random.permutation(len(x))
#     test_ratio = 0.2
#     test_size = int(len(x) * test_ratio)
#     test_index = shuffle_indexs[:test_size]
#     train_index = shuffle_indexs[test_size:]

#     x_train = x[train_index]
#     y_train = y[train_index]

#     x_test = x[test_index]
#     y_test = y[test_index]

#     return x_train, x_test, y_train, y_test


# x_train, x_test, y_train, y_test = train_test_split(x, y, 0.2)

stand = StandardScaler()
stand.fit(x_train)

x_train_stand = stand.transform(x_train)
x_test_stand = stand.transform(x_test)
sgd_model = SGDRegressor(n_iter=1000)
sgd_model.fit(x_train_stand, y_train)
score = sgd_model.score(x_test_stand, y_test)
print(score)
