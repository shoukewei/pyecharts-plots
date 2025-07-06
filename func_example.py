from pyecharts.charts import Bar
from pyecharts import options as opts
from utils.utils import render_and_open

# Sample bar chart
bar = (
    Bar()
    .add_xaxis(["A", "B", "C", "D"])
    .add_yaxis("Example", [10, 20, 30, 40])
    .set_global_opts(title_opts=opts.TitleOpts(title="Sample Bar Chart"))
)

# Use the reusable function (just filename, no ./output/)
render_and_open(bar, "sample_bar_chart.html")