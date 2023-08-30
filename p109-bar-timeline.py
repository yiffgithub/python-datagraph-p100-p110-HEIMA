'''
演示基础柱状图的开发
'''
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
from pyecharts.charts import Timeline
from pyecharts.options import *
from  pyecharts.globals import ThemeType
#使用 bar构建基础柱状图
bar1 = Bar()
# add x-axis data
# add y-axis data
bar1.add_xaxis(["xiaolin","xiaojin","xiaofan"])
bar1.add_yaxis("height",[110,50,109], label_opts= LabelOpts(position="right"))
#reverse x-axis and y-axis
bar1.reversal_axis()
bar2= Bar()
# add x-axis data
# add y-axis data
bar2.add_xaxis(["xiaolin","xiaojin","xiaofan"])
bar2.add_yaxis("height",[120,110,119], label_opts= LabelOpts(position="right"))
#reverse x-axis and y-axis
bar2.reversal_axis()

bar3 = Bar()
# add x-axis data
# add y-axis data
bar3.add_xaxis(["xiaolin","xiaojin","xiaofan"])
bar3.add_yaxis("height",[170,150,199], label_opts= LabelOpts(position="right"))
#reverse x-axis and y-axis
bar3.reversal_axis()
#creat timeline
Timeline=Timeline({"theme":ThemeType.LIGHT})
Timeline.add(bar1,"2000")
Timeline.add(bar2,"2002")
Timeline.add(bar3,"2005")
#set auto play
Timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)


# draw the bar 是用时间线对象绘图，而不是bar对象
Timeline.render("时间线基础柱状图.html")