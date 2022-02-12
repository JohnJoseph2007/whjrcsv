import pandas as pd

# Set Up:
df = pd.read_csv("data.csv")
data = df['Weight(Pounds)'].tolist()

# mean:
mean = sum(data)/len(data)
print(mean)