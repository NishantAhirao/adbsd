import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('HR.csv')
df
#print(df.shape)
#print(df.info)
print(df.columns)

#Mean of monthly income and age
print("The mean of monthly income is :",df.loc[:,"MonthlyIncome"].mean()) #loc[:, "MonthlyIncome"] is pandas DataFrame indexing operation that selects all rows and a specific column from the DataFrame based on label indexing
print("The mean of age is :",df.loc[:,"Age"].mean())

#Mode of monthly income and age
print("The median of monthly income is :",df.loc[:,"MonthlyIncome"].median())
print("The median of age is :",df.loc[:,"Age"].median())

#Median of monthly income and age
print("The mode of monthly income is :",df.loc[:,"MonthlyIncome"].mode())
print("The mode of age is :",df.loc[:,"Age"].mode())

#Standard deviation of monthly income and age
print("The standard deviation of monthly income is :",df.loc[:,"MonthlyIncome"].std())
print("The standard deviation of age is :",df.loc[:,"Age"].std())

#Storing age and monthly income in array and then finding maximum and minimum values
array1 = np.array(df['MonthlyIncome'])
array2=np.array(df["Age"])

print("Income",array1)
print("Age array",array2)
print("Maximum income among the employees is :",max(array1))
print("Minimum income among the employees is :",min(array1))
print("Maximum age among the employees is :",max(array2))
print("Minimum age among the employees is :",min(array2))

# Replacing the categorical values by numeric values
df.head()
df["BusinessTravel"].replace({"Travel_Rarely":1, "Travel_Frequently":0}, inplace=True)

# In this case, it replaces the values "Travel_Rarely" with 1 and "Travel_Frequently" with 0 in the "BusinessTravel" column.
#The inplace=True parameter specifies that the replacement should be performed directly on the DataFrame df instead of returning a new DataFrame.


df["Attrition"].replace({ "Yes":1, "No":0}, inplace=True)
df.head()