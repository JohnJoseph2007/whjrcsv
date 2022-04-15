import pandas as pd
import plotly.express as px

df = pd.read_csv("regression.csv")

toefl = df["TOEFL Score "].tolist()
chance = df["Chance of Admit "].tolist()

fig = px.scatter(x=toefl, y=chance)
fig.show()

import numpy as np

m, c = np.polyfit(toefl, chance, 1)
yarray = []

for x in toefl:
  y = m*x+c
  yarray.append(y)

fig = px.scatter(x=toefl, y=chance)
fig.update_layout(shapes=[dict(
    type="line",
    x0=min(toefl), x1=max(toefl),
    y0=min(yarray), y1=max(yarray)
)])
fig.show()

x = 100
y = m*x+c
print(y*100, "%")