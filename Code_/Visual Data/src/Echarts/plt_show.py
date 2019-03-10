# import numpy as np
# import matplotlib.pyplot as plt
# import pylab as pl
# # from pyecharts import Pie
# # 画出3行2列的饼图

# labels = ['Flat', 'Reduce', 'Raise']
# # 321 > 3行2列第1个
# fig1 = pl.subplot(321)
# plt.pie([12, 1, 7], labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
# plt.axis('equal')
# plt.title("group A_20min")

# # 322 > 3行2列第2个
# fig2 = pl.subplot(322)
# plt.pie([2, 2, 1], labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
# plt.axis('equal')
# plt.title("group B_20min")

# # 323 > 3行2列第3个
# fig3 = pl.subplot(323)
# plt.pie([8, 2, 10], labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
# plt.axis('equal')
# plt.title("group A_60min")

# # 324 > 3行2列第4个
# fig4 = pl.subplot(324)
# plt.pie([2, 1, 2], labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
# plt.axis('equal')
# plt.title("group B_60min")

# # 325 > 3行2列第5个
# fig5 = pl.subplot(325)
# plt.pie([4, 1, 15], labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)  # startangle表示饼图的起始角度
# plt.axis('equal')  # 这行代码加入饼图不会画成椭圆
# plt.title("group A_70min")

# # 326 > 3行2列第6个
# fig6 = pl.subplot(326)
# plt.pie([3, 1, 1], labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
# plt.axis('equal')
# plt.title("group B_70min")

# pl.tight_layout()  # 布局方法
# #pl.savefig('D:\\2018TianChiGame\pyecharts_demo\\vc5.jpg', dpi=500)  # dpi实参改变图像的分辨率
# pl.show()  # 显示方法


import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

labels = ['success', 'failed', 'canceled', 'live', 'suspened', 'undifined']

fig1 = pl.subplot(221)
plt.pie([21717, 19153, 2932, 462, 126, 2227], labels=labels,
        autopct='%3.1f %%', shadow=True, startangle=90, pctdistance=1	)
plt.axis('equal')
plt.title("Music")


fig2 = pl.subplot(222)
plt.pie([10236, 19869, 3085, 448, 51, 462], labels=labels,
        autopct='%3.1f %%', shadow=True, startangle=90, pctdistance=1	)
plt.axis('equal')
plt.title("Publishing")


fig3 = pl.subplot(223)
plt.pie([21357, 29582, 5153, 498, 92, 849], labels=labels,
        autopct='%3.1f %%', shadow=True, startangle=90, pctdistance=1	)
plt.axis('equal')
plt.title("Film & Video ")


fig4 = pl.subplot(224)
plt.pie([9346, 12954, 4958, 460, 177, 1], labels=labels,
        autopct='%3.1f %%', shadow=True, startangle=90, pctdistance=1	)
plt.axis('equal')
plt.title("Games")

plt.show()
