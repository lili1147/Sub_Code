'''
Day5.py 中函数的详解
'''

# range函数的使用
for i in range(4):
    print(i)
    # 输出0，1，2，3

for i in range(1, 4):
    print(i)
    # 输出1，2，3


# numpy 中的concatenate的使用  简单使用
# import numpy as np
# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([[7, 8, 9]])
# c = np.concatenate((a, b), axis=0)  # 将a和b合并，axis=0 意为按行合并
# print(c)

# 输出
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8]])
d = np.concatenate((a, b.T), axis=1)  # 将a和b合并，axis=1 意为按列合并
print(d)


# 输出
# [[1 2 3 7]
#  [4 5 6 8]]
