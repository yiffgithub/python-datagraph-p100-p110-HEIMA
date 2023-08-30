import json
from pyecharts import options as opts
from pyecharts.charts import Graph

with open("weibo.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes, links, categories, cont, mid, userl = j

# Specify the name of the person you want to focus on
your_specific_name = "新浪体育"

# Filter nodes and links based on the specified name
filtered_nodes = [node for node in nodes if node["name"] == your_specific_name]
filtered_links = [link for link in links if link["source"] == your_specific_name]

c = (
    Graph()
    .add(
        "新浪微博",
        filtered_nodes,
        filtered_links,
        categories,
        repulsion=50,
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(title="Graph-微博转发关系图"),
    )
    .render("graph_weibo_specific.html")
)
