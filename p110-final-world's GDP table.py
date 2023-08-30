# 图表数据分析最终章：GPD动图开发
#final part of data analysis by making table: GPD taable creating
from pyecharts.charts import Bar , Timeline
from pyecharts.globals import *
from pyecharts.options import *

#read all data in csvfile
f = open("G:/data-process-data/1960-2019全球GDP数据.csv","r",encoding= "GB2312")
data_lines = f.readlines() #readline 返回的是字符串，同时需要每一行处理一次成为列表，所以用readline更好

#close the file
f.close()
#delete the fist raw
data_lines.pop(0)

#transfer data to dicts
# 转换数据为字典格式，格式为
# { 年份: [ [国家, gdp], [国家,gdp], ......  ], 年份: [ [国家, gdp], [国家,gdp], ......  ], ...... }
# { 1960: [ [美国, 123], [中国,321], ......  ], 1961: [ [美国, 123], [中国,321], ......  ], ...... }
#creat a dict
data_dict= {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    #*******************************
    #如何判断字典里是否已经存在了指定的key，比如字典里是否已经存在了1960年或者1964年
    #*****************************

    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year] = [

        ]
        data_dict[year].append([country,gdp])
# print(data_dict[year])
#create timeline target
#创建时间对象



timeline = Timeline({"theme":ThemeType.LIGHT})
#排序年份
sorted_year_list=sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key = lambda element : element[1], reverse=True)#拓展内容，排序GDP（列表里的一个元素）
    # get first 6 highest
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])#x add countries
        y_data.append(country_gdp[1]/1000000000)# y add gdp (billions)

    #构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(billions)",y_data,label_opts=LabelOpts(position="ri"
                                                                       "right"))
    #反转x和y轴
    bar.reversal_axis()
    #set the title for each year
    bar.set_global_opts(
        title_opts= TitleOpts(title=f"global GDP of {year}")
    )
    timeline.add(bar,str(year))


# for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
# 在for中，将每一年的bar对象添加到时间线中

# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
# 绘图
timeline.render("Top 8 countries in global GDP 1960-2019.html")