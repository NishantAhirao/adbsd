import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder


import matplotlib.pyplot as plt


df = pd.read_csv('/content/test.csv')

print(df)

labelencoder = LabelEncoder()


df['Gender'] = labelencoder.fit_transform(df['Gender'])

df

df['Math Score'].plot(kind='box',title='math_score')

x = ['Math Score','Writing Score','Placement Count','Reading Score']

df.boxplot(x)

import scipy.stats as stats 

 

df['math_zscore'] = stats.zscore(df['Math Score'])


df

a = df['Math Score']
b = df['Reading Score']
plt.scatter(a,b)
print(stats.iqr(a, interpolation = 'midpoint'))

plt.show()
df