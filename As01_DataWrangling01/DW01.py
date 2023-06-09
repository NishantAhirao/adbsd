import numpy as np
import pandas as pd

df = pd.read_csv("Iris.csv")  # Read Dataset File

df  #print all dataset

df.head()   # read the first five rows

df.tail() # read the last five rows  

df.index #read index

df.columns # read columns

df.dtypes # read datta type

df.columns.values # returns array of columns

df.columns.values.tolist()  # return a list of column names

df.describe(include='all')  #describe the properties of data

# Read Data Column wise
df['Id']



df.describe()#describe the properties of data

df.shape  # check out the dimension of the dataset rows and columns

df.isnull().sum()  # knowing how many missing values in the data

df1 = df.fillna(value=0)  #filling missing value using fillna()   # Filling null values with a single value

df1.head()

#filling null value with the mean/max/min value of a column

df2=df.fillna(value=df["sepal_length"].mean())
df2.head()

df3=df.fillna(value=df["sepal_length"].min())
df3.head()

df3=df.fillna(value=df["sepal_width"].max())
df3.head()

#Drop such missing value use dropna() function
df4=df.dropna()
df4.head()


# //dtype() to check data type
# //astype() to change Data type
df["petal_length"]=df["petal_length"].round(0).astype(int)
print(df["petal_length"].dtypes)

df.head()



df.dtypes

# to convert categorical variables into quantitative variables in python

df["Code"]=pd.factorize(df.species)[0]
df.species.value_counts()