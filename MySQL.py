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
sql = "SELECT * FROM `257` ORDER By ID DESC LIMIT 200"
try:
    cursor.execute(sql)
    res = cursor.fetchall()
except:
    print("错误")
temp = []

#气温 地温 风速262、 风向261、气压260、太阳辐射、降水量、蒸发量、湿度


for row in res:
    id = row[0]
    temp += [row[1]]
    author = row[2]

    print('温度是：'+str(row[1]))
print(temp)





'''
fig = go.Figure(data=go.Bar(y=temp))
fig.show()
fig = px.bar_polar(wind, r="frequency", theta="direction",
                   color="strength", template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)
fig.show()
fig.add_trace(go.Barpolar(
        r=[row[1]],
        # name='11-14 m/s',
        marker_color='rgb(106,81,163)'
    ))
fig.update_traces(text=['北', '东北', '东', '东南', '南', '西南', '西北', '西'])
fig.update_layout(
    title='实验中学气象站',
    font_size=16,
    legend_font_size=16,
   # polar_radialaxis_ticksuffix='%',
   # polar_angularaxis_rotation=90,
)
fig.show()
'''