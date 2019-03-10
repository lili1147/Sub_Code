# from pyecharts import Map

# value = [155, 10, 66, 78]
# attr = ["福建", "山东", "北京", "上海"]
# map = Map("全国地图示例", width=1200, height=600)
# map.add("", attr, value, maptype='china')
# map.render()


from pyecharts import Map

# value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
# attr = [
#     "福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"
# ]
# map = Map("Map 结合 VisualMap 示例", width=1200, height=600)
# map.add(
#     "",
#     attr,
#     value,
#     maptype="china",
#     is_visualmap=True,
#     visual_text_color="#000",
# )
# map.render()


value = [27444, 256816, 11962, 524, 6219, 1741, 2666, 575, 1358,
         212, 1259, 1890, 2252, 1132, 470, 374, 400, 822, 97, 40, 118]
attr = ['United Kingdom', 'United States', 'Canada', 'Norway', 'Australia', 'Italy', 'Germany',
        'Ireland', 'Spain', 'Mexico', 'Sweden', 'France', 'Netherlands', 'New Zealand', 'Switzerland',
        'Austria', 'Belgium', 'Denmark', 'China', 'Luxembourg', 'Singapore']
map = Map("国家众筹项目数对比", width=1200, height=600)
map.add(
    "",
    attr,
    value,
    maptype="world",
    is_visualmap=True,
    visual_text_color="#000",
    is_map_symbol_show=False,
    visual_range=[40, 2000]
)

map.render()


# {'GB': 27444, 'US': 256816, 'CA': 11962, 'NO': 524, 'AU': 6219, 'IT': 1741,
#  'DE': 2666, 'IE': 575, 'ES': 1358, 'N,"0': 3785, 'MX': 212, 'SE': 1259,
#  'FR': 1890, 'NL': 2252, 'NZ': 1132, 'CH': 470, 'AT': 374,
#  'BE': 400, 'DK': 822, 'HK': 97, 'LU': 40, 'SG': 118}

# GB  英国
# US  美国
# CA  加拿大
# NO  挪威
# AU  澳大利亚
# IT  意大利
# DE	德国
# IE 	爱尔兰
# ES  西班牙
# MX  墨西哥
# SE  瑞典
# FR  法国
# NL  荷兰
# NZ  新西兰
# CH  瑞士
# AT  奥地利
# BE  比利时
# DK  丹麦
# HK  中国香港
# LU  卢森堡
# SG  新加坡
