#Step 1: Importing the Libraries#


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Step 2: Importing the dataset#

df = pd.read_csv("Iris.csv")
df.head()

#Step 3: Checking for null values#

df.isnull().sum()

x = df.iloc[:,:4].values
y = df['species'].values

#Step 4: Splitting the dataset into the Training set and Test set#

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

#Step 5: Feature Scaling#


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

#Step 6: Training the Naive Bayes Classification model on the Training Set#

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train, y_train)

#Step 7: Predicting the Test set results#

y_pred = classifier.predict(x_test) 
y_pred

#Step 8: Confusion Matrix and Accuracy#

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
from sklearn.metrics import accuracy_score 
print ("Accuracy : ", accuracy_score(y_test, y_pred))
cm

#Step 9: Comparing the Real Values with Predicted Values#

df = pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred})
df.head()