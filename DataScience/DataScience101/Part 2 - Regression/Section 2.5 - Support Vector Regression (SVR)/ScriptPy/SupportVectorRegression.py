# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:24:41 2020

@author: niccolo
"""

# Support Vector Regression
'''
Enter Support Vector Regression. SVR gives us the flexibility to define how much error is acceptable in our model and will find an appropriate line 
(or hyperplane in higher dimensions) to fit the data.
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir('C:\\Users\\niccolo\\Desktop\\DataScience101\\Part 2 - Regression\\Section 2.5 - Support Vector Regression (SVR)')
    
# import dataset
dataset = pd.read_csv('./Data/Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values # trick to force a Matrix with only one column
y = dataset.iloc[:, 2:].values # matrix of indipendent variable


# feature scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y)
y = y[:,0]


# Fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf') # Kernel might be linear,polynomial o gaussian(rbf)
regressor.fit(x, y)


# Predicting New Results
# need to inverse since is a transform value + need to create an array of one value
y_pred=sc_y.inverse_transform(regressor.predict(sc_x.transform(np.array([[6.5]]))))


# Visualizing the SVR
plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(x), color='blue')
plt.title('Truth or Bluff  (SVR Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


# Visualizing the SVR HD
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x,y,color='red')
plt.plot(x_grid,regressor.predict(x_grid), color='blue')
plt.title('Truth or Bluff  (SVR Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()