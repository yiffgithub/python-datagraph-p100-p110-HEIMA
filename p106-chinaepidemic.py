import json
from pyecharts.charts import Map
from pyecharts.options import *

# read all data in the file of 疫情.txt
f = open("G:\data-process-data/疫情.txt", "r", encoding="UTF-8")
data = f.read()
# close the file
f.close()
# now we have already get all the data, we need to transfer it to dics in python
data_dict = json.loads(data)
# 从字典中取出省份的数据
province_data_list = data_dict["areaTree"][0]["children"]
#print(province_data_list)
# 创建map图标需要列表作为data，所以哦组装每个省份和确诊人数为元组
# 再将各个省的数据都封装在列表内
# print(province_data_list)


    # 问题出在以下这行条件判断语句上：
    #
    # python
    # Copy
    # code
    # if province_data["name"] == "天津" or "北京" or "重庆" or "上海":
    #     这个条件判断不会按你的意图工作。在Python中，这个条件判断实际上等同于：
    #
    #     python
    #     Copy
    #     code
    #     if (province_data["name"] == "天津") or ("北京") or ("重庆") or ("上海"):
    #         因此，不管
    #         province_data["name"]
    #         的值是什么，这个条件都会被视为True。这就是为什么只有
    #         "天津"、"北京"、"重庆"、"上海"
    #         这几个地区被包括在内的原因。
    #
    #         你应该将条件判断写成以下形式，对每个省份的名称进行逐一比较：
    #
    #         python
    #         Copy
    #         code
    #         if province_data["name"] == "天津" or province_data["name"] == "北京" or province_data["name"] == "重庆" or
    #                 province_data["name"] == "上海":
    #             或者更简洁的方式是使用 in 运算符来检查名称是否在指定的省份列表中：
    #
    #             python
    #             Copy
    #             code
    #             if province_data["name"] in ["天津", "北京", "重庆", "上海"]:
    #                 同样的问题也存在于其他地区的判断中。修复这些条件判断后，你的代码应该能够正确处理所有省份的数据。
data_list = []
for province_data in province_data_list:
    if province_data["name"] == "天津" or province_data["name"] == "北京" or province_data["name"] == "重庆" or province_data["name"] == "上海":
        province_name = province_data["name"] + "市"
    elif province_data["name"] == "广西":
        province_name = province_data["name"]+"壮族自治区"
    elif province_data["name"] == "宁夏":
        province_name = province_data["name"]+"回族自治区"
    elif province_data["name"] == "新疆":
        province_name = province_data["name"] + "维吾尔自治区"
    elif province_data["name"] == "内蒙古" or province_data["name"] == "西藏":
        province_name = province_data["name"] + "自治区"

    else:
        province_name = province_data["name"] + "省"

    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))
print(data_list)
map = Map()
map.add("各省份确诊人数", data_list, "china")
# 全局设置
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFCC00"},  # 更改颜色
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF6600"},  # 更改颜色
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF3300"},  # 更改颜色
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#FF0000"},  # 更改颜色
            {"min": 100000, "label": "100000+人", "color": "#990000"}  # 更改颜色
        ]

    )
)
# draw the map
map.render("全国疫情地图.html")
