import numpy as np
import pandas as pd

df = pd.read_csv('output/predictions.txt', sep=' ')
df.score = df.score + np.random.random(len(df))*0.5
df.to_csv('output/predictions.txt', sep=' ', index=False)
