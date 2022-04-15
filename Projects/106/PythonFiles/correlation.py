import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

coffee = df['Coffee in ml'].tolist()
sleep = df['sleep in hours'].tolist()

correlation = np.corrcoef(coffee, sleep)
print(correlation)

fig = px.line(x=coffee, y=sleep)
fig.show()