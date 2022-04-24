import pandas as pd
import statistics as s
import random as r
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
responses = df["responses "].tolist()
# responses1 = [int(x) for x in responses]

sm = 0

df2 = pd.read_csv("data2.csv")
newsample = df2["reading_time"].tolist()
newsamplemean = s.mean(newsample)

rmean = s.mean(responses)
print(f"Mean of entire population: {rmean}")
sd = s.stdev(responses)

def sampling(count):
  listofsamples = []
  for i in range(count):
    random = r.randint(0, len(responses))
    value = responses[random-1]
    listofsamples.append(value)
  samplemean = s.mean(listofsamples)
  sm = samplemean
  return samplemean

def creategraph(data):
  sd1l, sd1h = rmean-sd, rmean+sd
  sd2l, sd2h = rmean-(2*sd), rmean+(2*sd)
  sd3l, sd3h = rmean-(3*sd), rmean+(3*sd)
  fig = ff.create_distplot([data], ["sample"], show_hist=False)
  fig.add_trace(go.Scatter(x=[sm, sm], y=[0, 0.50], mode="lines", name="Mean of Sample Data"))
  fig.add_trace(go.Scatter(x=[newsamplemean, newsamplemean], y=[0, 0.50], mode="lines", name="Mean of New Sample Data"))
  fig.add_trace(go.Scatter(x=[sd1l, sd1l], y=[0, 0.50], mode="lines", name="Low STDEV 1"))
  fig.add_trace(go.Scatter(x=[sd2l, sd2l], y=[0, 0.50], mode="lines", name="Low STDEV 2"))
  fig.add_trace(go.Scatter(x=[sd3l, sd3l], y=[0, 0.50], mode="lines", name="Low STDEV 3"))
  fig.add_trace(go.Scatter(x=[sd1h, sd1h], y=[0, 0.50], mode="lines", name="High STDEV 1"))
  fig.add_trace(go.Scatter(x=[sd2h, sd2h], y=[0, 0.50], mode="lines", name="High STDEV 2"))
  fig.add_trace(go.Scatter(x=[sd3h, sd3h], y=[0, 0.50], mode="lines", name="High STDEV 3"))
  fig.show()

def setup():
  means=[]
  for i in range(100):
    meanlist = sampling(30)
    means.append(meanlist)
  creategraph(means)
  meanofsamples = s.mean(means)
  print(f"Mean of samples: {meanofsamples}")
  zscore = (newsamplemean-sm)/sd
  print(f"Z-Score is {zscore}")

setup()