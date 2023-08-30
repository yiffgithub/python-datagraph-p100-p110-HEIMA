# 数据可视化之生成中国地图
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map = Map()

# prepare data
data = [
    ("北京市", 99), ("上海市", 512), ("重庆市", 5456), ("台湾省", 541), ("天津市", 5252)
]
# add data
map.add("测试地图", data, "china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,  # this is for color
        is_piecewise=True,  # this is for customize color
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999", "color": "#990033"},

        ]
    )
)
#draw map

map.render("p105-map.html")
