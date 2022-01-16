import pandas as pd
import plotly.express as px

df1 = pd.read_csv("graph1.csv")
df2 = pd.read_csv("graph2.csv")

px.bar(df1, x="Country", y="Per capita income", color="Year", title="Country money shit").show()
px.bar(df1, x="Country", y="Per capita income", color="Year", title="Country money shit").show()
px.bar(df2, x="Country", y="InternetUsers").show()