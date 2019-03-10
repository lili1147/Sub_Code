'''
调用自己实现的LogisticRegerssion
'''

import numpy as np
import matplotlib.pyplot as plt

import My_LogisticReression

from sklearn import datasets

# 导入鸢尾花的数据集

iris = datasets.load_iris()
# print(iris)

X = iris.data
y = iris.target

# 测试二分类 鸢尾花数据集是有三种分类，所以需要划分数据集

X = X[y < 2, :2]  # 只取 y=1和 y=2  还有只取前两个特征
y = y[y < 2]
# print(X.shape)


# 绘制散点图

plt.scatter(X[y == 0, 0], X[y == 0, 1], color='red')
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='blue')
# plt.show()


# 调用自己的逻辑回归算法

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666, test_size=0.2)

losgistic = My_LogisticReression.LogisticRegression()

losgistic.fit(X_train, y_train)

prop = losgistic.predict_prop(X_test)
print(prop)

vector = losgistic.predict(X_test)
print(vector)

score = losgistic.score(X_test, y_test)
print(score)
