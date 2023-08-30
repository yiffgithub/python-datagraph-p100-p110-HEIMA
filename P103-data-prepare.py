'''
演化可视化需求1：折线图开发
'''
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts
# 处理数据
f_us = open("G:\data-process-data/美国.txt","r", encoding= "UTF-8")
us_data = f_us.read() #read all data
f_jp = open("G:/data-process-data/日本.txt","r", encoding= "UTF-8")
jp_data = f_jp.read() #read all data
f_in = open("G:/data-process-data/印度.txt","r", encoding= "UTF-8")
in_data = f_in.read() #read all data

#eliminate not standard json data:beginning
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
#eliminate not standard json data:ending
us_data=us_data[:-2]
jp_data=jp_data[:-2]
in_data=in_data[:-2]
# 在Python中，切片操作用于从序列（比如字符串、列表等）中选择一个子序列。切片操作的一般形式是[start:stop]，其中start是起始索引（包含在切片中），而stop是结束索引（不包含在切片中）。
#
# 如果省略start，则切片从序列的开头开始。
# 如果省略stop，则切片从序列的末尾结束。
# 如果同时省略start和stop，则切片会复制整个序列。
#json 转python 字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# print(type(us_dict))
# print(us_dict)
#获取trend key
trend_data_us = us_dict['data'][0]['trend']
trend_data_jp = jp_dict['data'][0]['trend']
trend_data_in = in_dict['data'][0]['trend']
#获取日期数据，用于x轴，去到2020年（到314就结束 0 -314）
x_data_us = trend_data_us['updateDate'][:314]
x_data_jp = trend_data_jp['updateDate'][:314]
x_data_in = trend_data_in['updateDate'][:314]

#获取确诊数据，用于y轴去到2020年（到314就结束
y_data_us = trend_data_us['list'][0]['data'][:314]
y_data_jp = trend_data_jp['list'][0]['data'][:314]
y_data_in = trend_data_in['list'][0]['data'][:314]

#create table
line = Line()
#add x axis data 因为x轴是通用的，就是日期，所以我们只需要加一个就好了
line.add_xaxis(x_data_us)
#add y axis
#LabelOpts=LabelOpts(is_show = False)的意思就是不显示具体的折线图上面的数字，电视鼠标移到上面还是会显示
line.add_yaxis("美国确诊人数",y_data_us,label_opts=LabelOpts(is_show = False))
line.add_yaxis("日本确诊人数",y_data_jp,label_opts=LabelOpts(is_show = False))
line.add_yaxis("印度确诊人数",y_data_in,label_opts=LabelOpts(is_show = False))
#设置一下全局设置（加一个标题）
line.set_global_opts(
    #标题设置
    title_opts=TitleOpts(title="2020年美日印三国新馆确诊人数对比折线图", pos_right= "center",pos_bottom="1%")
)
# 调用render方法，生成图标
line.render("p103.html")
# 关闭文件
f_us.close()
f_jp.close()
f_in.close()


