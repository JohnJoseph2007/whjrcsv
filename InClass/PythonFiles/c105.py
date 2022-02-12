import csv
import math
import statistics as s

with open("data.csv") as f:
  df = csv.reader(f)
  listvar = list(df)

# Standard Deviation = sqrt(sigma(xi-mean)^2/n-1), where xi is each datapoint, mean is mean and n is the length of the array.
# Sigma is a for loop.

normallist = listvar[0]
array = []
for i in normallist:
  i = float(i)
  array.append(i)
mean = s.mean(array)
print(mean)

sqlist = []
for i in array:
  xi = (i-mean)**2
  sqlist.append(xi)

summation = 0
for i in sqlist:
  summation+=i

nonroot = summation/(len(array)-1)
sigma = math.sqrt(nonroot)

print("Standard Deviation = ", sigma)