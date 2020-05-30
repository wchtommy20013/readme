# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 19:16:33 2018

@author: nbenvenuti
"""

# RANDOM FOREST REGRESSION

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir('C:\\Users\\nbenvenuti\\Desktop\\Tutorial PyR\\Machine Learning\\Part 2 - Regression\Section 2.5 - Support Vector Regression (SVR)')
    
# import dataset
dataset = pd.read_csv('./Data/Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values # trick to force a Matrix with only one column
y = dataset.iloc[:, 2].values # matrix of indipendent variable


# Splitting Dataset into the training and test set
# in this case we have to few lines to perform it
"""from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size=0.2, random_state=0)"""

# feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y)
y = y[:,0]"""


# Fitting RF to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=300, criterion='mse',                                  random_state = 0)
regressor.fit(x, y)


# Predicting New Results
# need to inverse since is a transform vallue + need to create an array of one value
y_pred=regressor.predict(6.5)


# Visualizing the Random Forest
plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(x), color='blue')
plt.title('Truth or Bluff  (Deision Tree Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


# Visualizing the Random Forest HD
x_grid = np.arange(min(x), max(x), 0.01)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x,y,color='red')
plt.plot(x_grid,regressor.predict(x_grid), color='blue')
plt.title('Truth or Bluff  (Deision Tree Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


