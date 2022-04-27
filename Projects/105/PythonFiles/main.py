import pandas as pd
import plotly.express as px
import statistics as s
import math

df = pd.read_csv("data.csv")
dflist = df["data"].tolist()
print(dflist)

mean = s.mean(dflist)

sigma = 0
squared = 0
for i in dflist:
  x = i-mean
  squared = pow(x, 2) 
  sigma = sigma + squared

divide = sigma/len(dflist)
stdev = math.sqrt(divide)
print(stdev)
