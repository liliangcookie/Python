import pyecharts.options as opts
from pyecharts.charts import Line

from pyecharts.charts import Gauge
import pymysql
#wind = px.data.wind()
#fig = go.Figure()

conn = pymysql.connect(
    host = '39.98.227.158',
    user = 'root',
    password = 'xiaoqian1988',
    database = 'lwmos',
    charset='utf8'
)
print(conn)
# 链接游标是社么鬼
cursor = conn.cursor()
sql = "SELECT * FROM `257` order by id DESC limit 1 "
try:
    cursor.execute(sql)
    res = cursor.fetchall()
except:
    print("错误")
temp = []
time1 = []

#气温 地温 风速262、 风向261、气压260、太阳辐射、降水量、蒸发量、湿度
for row in res:
    id = row[0]
    temp += [row[1]]
    time1 += [row[2]]

    print('温度是：'+str(row[1]))
print(temp)

x_data = time1
y_data = temp


(
    Line()
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .render("温度.html")
    #.render("basic_line_chart.html")

)


c = (
    Gauge()
    .add(
        "实时气压",
        [("校园实时气压/hP", 1006)],
        min_ = 950,
        max_= 1050,
        split_number=10,
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
            )
        ),
        detail_label_opts=opts.LabelOpts(formatter="{value}"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="实验中学气象站--气压监测"),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .render("气压.html")
   # .render("gauge_splitnum_label.html")
)