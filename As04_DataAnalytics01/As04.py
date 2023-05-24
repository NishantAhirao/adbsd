import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Boston.csv")

df.head()

df.isna().sum()

target_variables = "medv"

y = df[target_variables]

x = df.drop(target_variables, axis=1)

x.head()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 2)

from sklearn.linear_model import LinearRegression

regression = LinearRegression()

regression.fit(x_train, y_train)

train_score=round(regression.score(x_train,y_train)*100,2)
print(train_score)

y_pred = regression.predict(x_test)

print(y_pred)

from sklearn.metrics import r2_score

score=round(r2_score(y_test,y_pred)*100,2)
print(score)

from sklearn import metrics
print("mean absolute error on test data of linear regression", metrics.mean_absolute_error(y_test,y_pred))

print("mean squared eror on test data of linear regression", metrics.mean_squared_error(y_test, y_pred))

print("root mean squared error on test data of linear regression",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

df = pd.DataFrame({"actual":y_test, "predicted":y_pred, "variance":y_test-y_pred})

df.head()