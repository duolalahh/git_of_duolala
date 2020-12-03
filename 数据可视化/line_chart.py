import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
from page_while import sexlist,datetolist
from page_while import male,female,year,date,age_rank

suicides_100k=date['suicides/100k pop'].groupby(date['year']).mean()
year=[str(i)+"年" for i in range(1985,2017) if i%2==0]
line=(
    Line()
    .add_xaxis(year)
    .add_yaxis("世界自杀率",datetolist(suicides_100k),is_connect_nones=True)
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name="每100k人中自杀人数",
            min_=11,
            max_=17,
            position="left",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#675bba")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} 人/100k"),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        ),
        title_opts=opts.TitleOpts(title="worldwide suicides by year"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),)
    .render("line_chart.html")
)