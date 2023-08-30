# pycharm基础入门-折线图
#
# 导包
from pyecharts.charts import Line
# 创建一个折线图对象
Line = Line()
# 添加x轴数据
Line.add_xaxis(["xiaoquan","xiaolin","xiaoshan"])
# 添加y轴数据
Line.add_yaxis("height",[180,220,130])
# 通过render（渲染）方法生成html文件
#
Line.render()