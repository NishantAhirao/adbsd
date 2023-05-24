#Step 1: Importing the Libraries#


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

#Step 2: Importing the dataset#

dataset = sns.load_dataset('titanic')
dataset.head()

#Step 3: Plotting different graphs#

#Distplot#

sns.distplot(x = dataset["age"], bins = 10)

#Joint Plot#


sns.jointplot(x=dataset["age"],y=dataset["fare"],kind="scatter")


sns.jointplot(x = dataset["age"], y = dataset["fare"], kind = "hex")

#Rug Plot#

sns.rugplot(dataset["fare"])

#Bar Plot#

sns.barplot(x="sex", y="age", data=dataset)

#Count Plot#

sns.countplot(x="sex", data=dataset)

#Box Plot#

sns.boxplot(x="sex", y="age", data=dataset)

#Violin Plot#

sns.violinplot(x="sex", y="age", data=dataset)

#Strip Plot#

sns.stripplot(x="sex", y="age", data=dataset, jitter=False)

#Swarm Plot#

sns.swarmplot(x="sex", y="age", data=dataset)

#Heat Maps#

dataset = sns.load_dataset("titanic")
dataset.head()

corr = dataset.corr()
sns.heatmap(corr)

#Checking how the price of the ticket (columname:"fare") for each passenger is distributed by plotting a historgram#

sns.histplot(dataset["fare"],kde=False,bins=10)

