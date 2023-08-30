'''
演示基础柱状图的开发
'''
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
from pyecharts.options import *
#使用 bar构建基础柱状图
bar = Bar()
# add x-axis data
# add y-axis data
bar.add_xaxis(["xiaolin","xiaojin","xiaofan"])
bar.add_yaxis("height",[170,150,199], label_opts= LabelOpts(position="right"))
#reverse x-axis and y-axis
bar.reversal_axis()
# draw the bar
bar.render("基础柱状图.html")