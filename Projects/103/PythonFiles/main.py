import pandas as p
import plotly.express as px

df = p.read_csv("csv103.csv")

graph = px.scatter(df, "date", "cases", "country")
graph.show()