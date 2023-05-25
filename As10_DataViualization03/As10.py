import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv('/content/Iris.csv') 
df1

df = pd.DataFrame(df1)
df.head()

df.describe()

df.info()

df.columns

df['SepalLengthCm'].max()

df['SepalLengthCm'].min()

df['SepalLengthCm'].hist(bins = 30)

df['PetalLengthCm'].max()

df['PetalLengthCm'].min()

df['PetalLengthCm'].hist(bins = 30)

df['PetalWidthCm'].max()

df['PetalWidthCm'].min()

df['PetalWidthCm'].hist(bins = 30)

df['SepalWidthCm'].max()

df['SepalWidthCm'].min()

df['SepalWidthCm'].hist(bins = 30)

df['Species'].value_counts()

df['Species'].hist(bins = 30) #create histogram with 30 bins

sns.boxplot(x = 'SepalLengthCm' ,data = df)

sns.boxplot(x = 'SepalWidthCm' , data = df)

sns.boxplot(x = 'PetalWidthCm' , data = df)

sns.boxplot(x = 'PetalLengthCm', data = df)