import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts

url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
df = pd.read_csv(url)

# Filter for world data
world_df = df[df['country'] == 'World']
world_df = world_df[['year', 'co2']].dropna()


line = (
    Line()
    .add_xaxis(world_df['year'].astype(str).tolist())
    .add_yaxis("CO₂ Emissions (billion tonnes)", world_df['co2'].round(2).tolist())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Global CO₂ Emissions Over Time"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(name="CO₂ (Gt)"),
        xaxis_opts=opts.AxisOpts(name="Year")
    )
)

line.render("co2_emissions.html")