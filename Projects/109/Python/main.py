import pandas as pd
import statistics as s

df = pd.read_csv("data.csv")
read = df["reading score"].tolist()

mean = s.mean(read)
median = s.median(read)
mode = s.mode(read)
stdev = s.stdev(read)

print(f"{mean} is the mean")
print(f"{median} is the median")
print(f"{mode} is the mode")
print(f"{stdev} is the standard deviation")

gen11, gen12 = mean-stdev, mean+stdev
gen21, gen22 = mean-(2*stdev), mean+(2*stdev)
gen31, gen32 = mean-(3*stdev), mean+(3*stdev)

s1 = [x for x in read if x>gen11 and x<gen12]
s2 = [x for x in read if x>gen21 and x<gen22]
s3 = [x for x in read if x>gen31 and x<gen32]

p1 = (len(s1)/len(read))*100
p2 = (len(s2)/len(read))*100
p3 = (len(s3)/len(read))*100

print("------------------------------------")
print(f"{p1}% of data lies between 1st standard deviation")
print(f"{p2}% of data lies between 2nd standard deviation")
print(f"{p3}% of data lies between 3rd standard deviation")