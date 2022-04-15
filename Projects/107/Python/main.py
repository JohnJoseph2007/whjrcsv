import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
group = df.groupby("level")["attempt"].mean()

fig = px.scatter(group, x=df["student_id"], y=df["level"], color=df["attempt"])
fig.show()