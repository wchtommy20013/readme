# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:31:05 2020

@author: niccolo
"""

# -*- coding: utf-8 -*-# Support Vector Regression
"""
Created on Fri Jul 27 18:39:31 2018

@author: nbenvenuti
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir('C:\\Users\\niccolo\\Desktop\\DataScience101\\Part 2 - Regression\\Section 2.6 - Decision Tree Regression')
    
# import dataset
dataset = pd.read_csv('./Data/Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values # trick to force a Matrix with only one column
y = dataset.iloc[:, 2].values # matrix of indipendent variable


# Fitting Decision tree to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0) # Default is MSE
regressor.fit(x, y)


# Predicting New Results
y_pred=regressor.predict([[6.5]])


# Visualizing the Deision Tree Regression HD
x_grid = np.arange(min(x), max(x), 0.01)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x,y,color='red')
plt.plot(x_grid,regressor.predict(x_grid), color='blue')
plt.title('Truth or Bluff  (Deision Tree Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

