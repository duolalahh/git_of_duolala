import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Bar,Timeline,Pie,Page,Line,Map
from pyecharts.globals import ThemeType

def datetolist(n):
    c=np.array(n)
    c_2f=np.round(c,2)
    c_tolist=c_2f.tolist()
    return c_tolist

def sexlist(sex):
    sex_suicides_100k=[]
    for i in year:
        sex_suicides=[]
        for j in sex:
            if i==j[1]:
                sex_suicides.append(j[4])
        sex_suicides=np.array(sex_suicides)
        sex_suicides=np.round(sex_suicides,2)
        np.seterr(invalid='ignore')
        mean=np.mean(sex_suicides)
        mean=np.round(mean,2)
        sex_suicides_100k.append(mean)
    return sex_suicides_100k

def sex_value(sex):
    sex_=np.array(sex)
    sex_sum=np.sum(sex_)
    return sex_sum

def bar_suicides_no():
    c=(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
    .add_xaxis(year)
    .add_yaxis("年均总自杀人数",datetolist(date_y))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全球范围"),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],  
        )
    )
    return c

def bar_suicides_100k():
    c=(
        Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
        .add_xaxis(year)
        .add_yaxis("male",sexlist(male))
        .add_yaxis("famale",sexlist(female))
        .set_global_opts(title_opts=opts.TitleOpts("男女自杀率对比"),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")], 
        )
    )
    return c

def timeline_suicides():
    t1=Timeline()
    for i in range(1985,2016):
        bar=(
            Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
            .add_xaxis(country20)
            .add_yaxis("15-24 years",shujizonghe[i][0::5])
            .add_yaxis("25-34 years",shujizonghe[i][1::5])
            .add_yaxis("35-54 years",shujizonghe[i][2::5])
            .add_yaxis("55-74 years",shujizonghe[i][3::5])
            .add_yaxis("75+ years",shujizonghe[i][4::5])
            .set_global_opts(title_opts=opts.TitleOpts("{}年男性自杀率".format(i)))
        )
        pie=(
            Pie()
            .add(
                "Austria",
                [list(z) for z in zip(age_rank, shujizonghe[i][0:5])],
                rosetype="radius",
                center=["80%", "20%"],
                radius="28%",
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="年龄段比重"))
        )
        bar.overlap(pie)
        t1.add(bar,"{}".format(i))
        t1.add_schema(is_auto_play=True, play_interval=1000, is_timeline_show=False)
    return t1


def map_world():
    c = (
        Map()
        .add("自杀率", [list(z) for z in zip(country, datetolist(country_y))], "world",is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="自杀率=自杀人数/100k"),
            visualmap_opts=opts.VisualMapOpts(max_=20,is_calculable=True,),
        )
    )
    return c

def page_layout():
    page=Page(layout=Page.DraggablePageLayout)
    page.add(
        map_world(),
        timeline_suicides(),
        bar_suicides_no(),
        bar_suicides_100k(),
    )
    page.render("page.html")

date=pd.read_csv("master.csv")
country20=['Austria', 'Belgium', 'Estonia', 'Finland', 'France', 'Hungary', 'Japan', 'Serbia', 'Ukraine',]
ls=[i for i in date['country']]
country=list(set(ls))
country.sort(key=ls.index)
suicides=[]
male=[]
female=[]
year=[i for i in range(1985,2017)]
date_y=date['suicides_no'].groupby(date['year']).sum()
country_y=date['suicides/100k pop'].groupby(date['country']).mean()
age_rank=['15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years']
date_value=date.iloc[[i for i in range(len(date))],[0,1,2,3,6]]
date_value=np.array(date_value).tolist()

for i in date_value:
    if i[0] in country20 and i[3]!='5-14 years' and i[2]=='male':
        suicides.append(i)
    if i[2]=="male":
        male.append(i)
    if i[2]=="female":
        female.append(i)
suicides.sort(key=lambda x: (x[0],x[1],x[3]))
whileyear=[]
for i in year:
    year_suicides=[]
    for j in suicides:
        if i==j[1]:
            year_suicides.append(j[4])
    whileyear.append(year_suicides)
shujizonghe=dict(zip(year,whileyear))
npshuju=np.array(whileyear)

#第二次运行时块注释以下内容 
""" if __name__=="__main__":
    page_layout() """

#第二次运行程序是取消以下注释
Page.save_resize_html("page.html",cfg_file="chart_config.json",dest="page_1.html")