from bokeh.plotting import figure, output_file, show
import pandas as pd
import sqlite3

con = sqlite3.connect("/Users/seungyong/workspace/sqlite/maruda.db")


df_sensor = pd.read_sql('select * from sensor_log', con)
df_sensor[['YMDMS', 'SENSOR_TYPE', 'SENSOR_DATA']].sort_values('YMDMS', ascending=True)
x = df_sensor['YMDMS']
y = df_sensor['SENSOR_DATA']

#x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
#y0 = [i**2 for i in x]
#y1 = [10**i for i in x]
#y2 = [10**(i**2) for i in x]

output_file("log_liens.html")

p = figure(
    tools="pan,box_zoom,reset,save",
    y_axis_type="log", y_range=[0.001, 10**11], title="log axis example",
    x_axis_label='selections', y_axis_label='particles'
)

p.line(x, x, legend="ultrasonic")

p.line(x, y, legend="IR", line_width=3)
p.line(x, y, legend="y=10^x", line_color="red")
p.line(x, y, legend="y=10^x^2", line_color="orange", line_dash="4 4")
#p.circle(x, x, legend="y=x", fill_color="white", size=8)
#p.circle(x, y1, legend="y=10^x", fill_color="red", line_color="red", size=6)
show(p)
