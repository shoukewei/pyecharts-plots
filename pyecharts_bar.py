import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

url = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
df = pd.read_csv(url)

latest = df[df['Year'] == 2023]
top10 = latest.sort_values(by='Value', ascending=False).head(10)


bar = (
    Bar()
    .add_xaxis(top10['Country Name'].tolist())
    .add_yaxis("Population", top10['Value'].tolist())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Top 10 Countries by Population (2023)"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)),
        datazoom_opts=opts.DataZoomOpts(),
    )
)
bar.render("./output/population_top10.html")