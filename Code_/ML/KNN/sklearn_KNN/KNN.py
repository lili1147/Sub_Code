from sklearn import datasets
from sklearn.model_selection import train_test_split
from KNNClassifiy import KNNClassifier
import numpy as np

iris = datasets.load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
my_knn = KNNClassifier()

# print(x_test)
y_predicts = []
for item in x_test:
    y_predict = my_knn.MyKnnClassifiy(x_train, y_train, item, 3)
    y_predicts.append(y_predict)


print(y_predicts)
print(y_test)
acc = np.sum(y_predicts == y_test)
print(acc)
print(len(y_test))
rate = acc / len(y_test)
print(rate)

# print(X)
# print(y)
# print(X.shape)
# print(X.shape[0])
# print(X.shape[1])
# print(y.shape)
