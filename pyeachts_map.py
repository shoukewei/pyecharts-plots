from pyecharts.charts import Map
from pyecharts import options as opts

gdp_data = {
    "United States": 26344,
    "China": 17938,
    "Japan": 4206,
    "Germany": 4223,
    "India": 3416,
    "United Kingdom": 3305,
    "France": 3061,
    "Italy": 2400,
    "Brazil": 2113,
    "Canada": 2253,
}


map_chart = (
    Map()
    .add("GDP (in billion USD)", [list(z) for z in gdp_data.items()], "world")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="World GDP by Country"),
        visualmap_opts=opts.VisualMapOpts(max_=27000),
    )
)
map_chart.render("world_gdp_map.html")