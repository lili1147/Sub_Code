from keras.datasets import boston_housing

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

print(train_data.shape)  # (404,13)
print(train_targets.shape)  # (404)
# for item in train_data:
#     print(item)

# print('-------------')
# for item in train_targets:
#     print(item)

# 准备数据
# 13个特征值，对特征值做标准化处理：减去平均值，再除以标准差

mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std

test_data -= mean
test_data /= std

from keras import models
from keras import layers
print(train_data.shape[1])  # 13 维度


def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))

    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model


# k折交叉验证

import numpy as np
k = 4
num_val_samples = len(train_data) // k
# num_epochs = 100
num_epochs = 500
# all_scores = []
all_mae_scores = []
for i in range(k):
    print('processing fold#', i)
    val_data = train_data[i * num_val_samples:(i + 1) * num_val_samples]
    val_targets = train_targets[i * num_val_samples:(i + 1) * num_val_samples]

    partial_train_data = np.concatenate(
        [train_data[:i * num_val_samples], train_data[(i + 1) * num_val_samples:]], axis=0)

    partial_train_targets = np.concatenate(
        [train_targets[:i * num_val_samples], train_targets[(i + 1) * num_val_samples:]], axis=0)

    model = build_model()
    # model.fit(partial_train_data, partial_train_targets, epochs=num_epochs, batch_size=1, verbose=0)
    history = model.fit(partial_train_data,
                        partial_train_targets,
                        validation_data=(val_data, val_targets),
                        epochs=num_epochs,
                        batch_size=1,
                        verbose=0
                        )
    # val_mse, val_mae = model.evaluate(val_data, val_targets, verbose=0)
    # all_scores.append(val_name)
    mae_history = history.history['val_mean_absolute_error']
    all_mae_scores.append(mae_history)

average_mae_history = [np.mean([x[i] for x in all_mae_scores]) for i in range(num_epochs)]

import matplotlib.pyplot as plt
plt.plot(range(1, len(average_mae_history) + 1), average_mae_history)
plt.xlabel('epochs')
plt.ylabel('mae')
plt.show()


# K折交叉验证

# k = 4
# examples_num = len(train_data) // k  # //双斜杠 向下取整

# epochs_tiems = 100

# for i in range(k):
#     val_data = train_data[i * examples_num:(i + 1) * examples_num]
#     partial_train_data = train_data.concatenate(
#         [train_data[:i * examples_num], train_data[(i + 1) * examples_num:]], axis=0
#     )

#     val_targets = train_targets[i * examples_num:(i + 1) * examples_num]
#     partial_train_targets = train_targets.concatenate(
#         [train_targets[:i * examples_num], train_targets[(i + 1) * examples_num]], axis=0
#     )
#     model = build_model()
#     model.fit(
#         partial_train_data,
#         partial_train_targets,
#         validation_data=(val_data, val_targets),
#         epochs=epochs_tiems,
#         batch_size=1
#     )
def smooth_curve(points, factor=0.9):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:
            smoothed_points.append(point)
    return smoothed_points
