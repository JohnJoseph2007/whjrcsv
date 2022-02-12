from collections import Counter
import pandas as pd

# Set Up:
df = pd.read_csv("data.csv")
datar = df['Weight(Pounds)'].tolist()
data = datar
data.sort()
print(data)

# mean:
mean = sum(data)/len(data)
print(mean)

# median:
middle = len(data)//2
if len(data)%2==0:
  median = (data[middle] + data[middle+1])/2
  print(median)
elif len(data)%2==1:
  median = data[middle]
  print(median)

# mode:
datacount = Counter(datar)
a = datacount.values()
maximum = max(a)
x = [i for i, frequency in datacount.items() if frequency==maximum]
print(*(x))