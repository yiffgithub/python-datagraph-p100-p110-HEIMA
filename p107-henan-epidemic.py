"""河南疫情地图开-演示"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("G:\data-process-data/疫情.txt", "r", encoding="UTF-8")
data = f.read()
# close the file
f.close()
# now we have already get all the data, we need to transfer it to dics in python
data_dict = json.loads(data)
#只要河南的数据
cities_data = data_dict["areaTree"][0]["children"][3]["children"]

#准备数据为元并放入list
data_list = []
for city_data in cities_data:
    city_name = city_data["name"]+"市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name,city_confirm))

data_list.append(("济源市",5))
# print(data_list)
map = Map()
map.add("河南省疫情分布", data_list,"河南")
# # 全局设置
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-10人", "color": "#CCFFFF"},
            {"min": 10, "max": 19, "label": "10-29人", "color": "#FFCC00"},  # 更改颜色
            {"min": 20, "max": 29, "label": "20-29人", "color": "#FF6600"},  # 更改颜色
            {"min": 30, "max": 39, "label": "30-39人", "color": "#FF3300"},  # 更改颜色
            {"min": 40, "max": 49, "label": "40-49人", "color": "#FF0000"},  # 更改颜色
            {"min": 50, "label": "50+人", "color": "#990000"}  # 更改颜色
        ]

    )
)
# draw the map
map.render("河南省疫情地图.html")
