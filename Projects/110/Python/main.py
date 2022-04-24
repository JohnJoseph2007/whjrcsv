import pandas as pd
import statistics as s
import random as r
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
responses = df["responses "].tolist()
# responses1 = [int(x) for x in responses]

rmean = s.mean(responses)
print(f"Mean of entire population: {rmean}")

def sampling(count):
  listofsamples = []
  for i in range(count):
    random = r.randint(0, len(responses))
    value = responses[random-1]
    listofsamples.append(value)
  samplemean = s.mean(listofsamples)
  return samplemean

def creategraph(data):
  fig = ff.create_distplot([data], ["sample"], show_hist=False)
  fig.show()

def setup():
  means=[]
  for i in range(100):
    meanlist = sampling(30)
    means.append(meanlist)
  creategraph(means)
  meanofsamples = s.mean(means)
  print(f"Mean of samples: {meanofsamples}")

setup()