import pandas as pd
import plotly.express as px
import numpy as np

#NEGATIVE CORRELATION
df = pd.read_csv("cups of coffee vs hours of sleep.csv")
coffee = df["Coffee in ml"].tolist()
sleep = df["sleep in hours"].tolist()
graph = px.scatter(x=coffee, y=sleep)
graph.show()

correlation = np.corrcoef(coffee, sleep)
print(correlation[-1,0])

#POSITIVE CORRELATION
df = pd.read_csv("Student Marks vs Days Present.csv")
coffee = df["Days Present"].tolist()
sleep = df["Marks In Percentage"].tolist()
graph = px.scatter(x=coffee, y=sleep)
graph.show()

correlation = np.corrcoef(coffee, sleep)
print(correlation[0,1])


#ZERO CORRELATION
df = pd.read_csv("c1.csv")
coffee = df["Size of TV"].tolist()
sleep = df["\tAverage time spent watching TV in a week (hours)"].tolist()
graph = px.scatter(x=coffee, y=sleep)
graph.show()

correlation = np.corrcoef(coffee, sleep)
print(correlation)