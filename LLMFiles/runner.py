
import pandas as pd
df = pd.read_csv("demo-audio-data.csv", header=None)
cutoff = 61766
filtered_numbers = df[df[0] > cutoff]
answer = filtered_numbers[0].sum()
print(answer)
