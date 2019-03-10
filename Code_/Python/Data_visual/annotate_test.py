'''
Matplotlib中的 annotate()详解
标记的作用
annotate()方法提供辅助函数，是标注变得容易。在标注中，需要考虑两点：一由参数xy表示标注位置和xytext的文本位置，
这两个参数都是（x,y）元组
'''

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(111)

x = np.arange(0.0, 5.0, 0.01)
y = np.cos(2 * np.pi * x)
x1 = np.arange(0.0, 5.0, 0.01)
y1 = np.sin(x1)
ax.plot(x, y, label='$sinx+1$', color='red', linewidth=2),
ax.plot(x1, y1, label='sinx', color='green', linewidth=2)


# xy=(横坐标，纵坐标)  箭头尖端
#    xytext=(横坐标，纵坐标) 文字的坐标，指的是最左边的坐标
#    arrowprops= {
#        facecolor= '颜色',
#        shrink = '数字' <1  收缩箭头
#    }

ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black',
                                                                     shrink=0.05))
ax.set_ylim(-2, 2)
plt.legend()
plt.show()
