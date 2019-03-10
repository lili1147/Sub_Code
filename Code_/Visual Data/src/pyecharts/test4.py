# from pyecharts import Pie

# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [11, 12, 13, 10, 10, 10]
# pie = Pie("饼图-圆环图示例", title_pos='center')
# pie.add(
#     "",
#     attr,
#     v1,
#     radius=[40, 75],
#     label_text_color=None,
#     is_label_show=True,
#     legend_orient="vertical",
#     legend_pos="left",
# )
# pie.render(path='pie.png')


from pyecharts import Pie

attr = ["时尚", "科技", "电影", "图书", "美食", "旅行"]
v1 = [11, 12, 13, 10, 10, 10]
v2 = [19, 21, 32, 20, 20, 33]
pie = Pie("饼图-玫瑰图示例", title_pos='center', width=900)
pie.add(
    "众筹",
    attr,
    v1,
    center=[25, 50],
    is_random=True,
    radius=[30, 75],
    rosetype="radius",
)
pie.add(
    "众筹",
    attr,
    v2,
    center=[75, 50],
    is_random=True,
    radius=[30, 75],
    rosetype="area",
    is_legend_show=False,
    is_label_show=True,
)
pie.render(path='pie2.png')
