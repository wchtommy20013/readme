# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:40:04 2020

@author: niccolo
"""

# Simple Linear Regression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir('C:\\Users\\niccolo\\Desktop\\DataScience101\\Part 2 - Regression\\Section 2.2 - Simple Linear Regression')

# import dataset
dataset = pd.read_csv('./Data/Salary_Data.csv')
x = dataset.iloc[:, :-1].values # matrix of dependent variable
y = dataset.iloc[:, 1].values # matrix of indipendent variable

# Splitting Dataset into the training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size=1/3, random_state=0)

# Fitting Simple Linear Regression to the training set 
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
regressor.score(X_train, Y_train)

# Formula
print('y = '+str(float(regressor.coef_))+'x + '+str(regressor.intercept_))

# Predict the test set 
y_pred = regressor.predict(X_test)
regressor.score(X_test, y_pred)


# Visualising the training set results
plt.scatter(X_train, Y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary Vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the test set results
plt.scatter(X_test, Y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary Vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


