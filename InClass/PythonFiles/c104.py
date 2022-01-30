from collections import Counter
import pandas as pd

a = pd.read_csv("./InClass/CSVFiles/c104.csv")
h = a["Height(Inches)"].tolist()
l = len(h)

# MEAN :
mean = sum(h)/l
#print(mean)

# MEDIAN :
if(l%2==0):
    m1 = float(h[l//2])
    m2 = float(h[l//2-1])
    median = (m1+m2)/2
else:
    median = h[l//2]
#print(median)

# MODE :
dummylist = [1, 2, 3, 4, 5, 6, 7, 1, 4, 2, 6, 6, 7,]
egdata = Counter(h)
e = egdata.values()
maxval = max(e)
x = [num for num, freq in egdata.items() if freq==maxval]
print(*(x))
