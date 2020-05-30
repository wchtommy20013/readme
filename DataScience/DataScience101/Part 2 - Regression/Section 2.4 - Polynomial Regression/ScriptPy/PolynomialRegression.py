# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:19:51 2020

@author: niccolo
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir('C:\\Users\\niccolo\\Desktop\\DataScience101\\Part 2 - Regression\\Section 2.4 - Polynomial Regression')

# import dataset
dataset = pd.read_csv('./Data/Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values # trick to force a Matrix with only one column
y = dataset.iloc[:, 2].values # matrix of indipendent variable


# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(x,y)


####################################
# Polynomial with 2 df
# Fitting Polynomial Regression to the dataset with 2 degrees
####################################
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=2)
x_ploy = poly_reg.fit_transform(x)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_ploy, y)

# Let's see which one between Linear and Polynomial Regression is fitting better
# Visualizing the linear regression results
plt.scatter(x,y,color='red')
plt.plot(x,lin_reg.predict(x), color='blue')
plt.title('Truth or Bluff  (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


# Visualizing the Polynomial regression results
plt.scatter(x,y,color='red')
plt.plot(x,lin_reg2.predict(poly_reg.fit_transform(x)), color='blue')
plt.title('Truth or Bluff  (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()



####################################
# Polynomial with 3 df
# Fitting Polynomial Regression to the dataset with 3 degrees
####################################
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=3)
x_ploy = poly_reg.fit_transform(x)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_ploy, y)

# Visualizing the Polynomial regression results with 3 df
plt.scatter(x,y,color='red')
plt.plot(x,lin_reg2.predict(poly_reg.fit_transform(x)), color='blue')
plt.title('Truth or Bluff  (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


####################################
# Polynomial with 4 df
# Fitting Polynomial Regression to the dataset with 3 degrees
####################################
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=4)
x_ploy = poly_reg.fit_transform(x)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_ploy, y)

# Visualizing the Polynomial regression results with 4 df
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x,y,color='red')
plt.plot(x_grid,lin_reg2.predict(poly_reg.fit_transform(x_grid)), color='blue')
plt.title('Truth or Bluff  (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

