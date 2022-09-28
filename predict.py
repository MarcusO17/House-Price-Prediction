# import numpy package for arrays and stuff
import numpy as np

# import matplotlib.pyplot for plotting our result
import matplotlib.pyplot as plt

# import pandas for importing csv files
import pandas as pd

from sklearn.tree import DecisionTreeRegressor

housing = pd.read_csv('housingData_clean.csv')
housing = housing.drop(['Title'],axis=1)
housing = housing.drop(housing.columns[0],axis=1)
print(housing.head())

X = housing[['BuildArea','Location','NoOfBedrooms','NoOfBathrooms']]
y = housing[['Price']]
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X,y)

y_pred =regressor.predict([[1141,19,2,1]])
print(y_pred)