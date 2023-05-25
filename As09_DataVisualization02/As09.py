import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df1 = sns.load_dataset('titanic') 
df1

df = pd.DataFrame(df1)
df.head()

df.describe()

df.info()

df.columns

sns.set_style('whitegrid') 
plt.figure(figsize = (10 , 4))
sns.boxplot(x = 'age' , y = 'sex' , data= df , hue = 'survived')
