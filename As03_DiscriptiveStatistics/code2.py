import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


df=pd.read_csv('Iris.csv',index_col='Id')
df

data=df

data["Species"].value_counts()
data.rename(columns={"SepalLengthCm":"slength","SepalWidthCm":"swidth","PetalLengthCm":"plength","PetalWidthCm":"pwidth"},inplace=True)
sum_data = data["slength"].sum()
mean_data = data["slength"].mean()
median_data = data["slength"].median()

print("sepal sum ", sum_data)
print("sepal mean",mean_data)
print("sepal median",median_data)

data.isnull()
data_satosa=data["Species"]=="Iris-setosa"
# creates a boolean Series named data_satosa by comparing the values in the "Species" column of the DataFrame data with the string "Iris-setosa".

print("for setosa")

print(data[data_satosa].describe())
data_satosa=data["Species"]=="Iris-virginica"

print('for virginica')
print(data[data_satosa].describe()) 
#  that computes descriptive statistics of a DataFrame or Series.
print('for versicolor')

data_satosa=data["Species"]=='Iris-versicolor'
print(data[data_satosa].describe())