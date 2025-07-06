from pyecharts.charts import Pie
from pyecharts import options as opts

data = [
    ("Chrome", 65.5),
    ("Safari", 18.7),
    ("Edge", 4.2),
    ("Firefox", 3.4),
    ("Others", 8.2),
]

pie = (
    Pie()
    .add("", data)
    .set_global_opts(title_opts=opts.TitleOpts(title="Browser Market Share"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)
pie.render("./output/browser_share.html")