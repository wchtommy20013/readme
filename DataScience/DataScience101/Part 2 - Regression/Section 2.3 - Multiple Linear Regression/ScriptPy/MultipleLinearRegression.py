# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:53:24 2020

@author: niccolo
"""

# Multiple Linear Regression

# Before prform multiple linear regression verify this assumption:
# 1) Linearity -- Linear relationship between dependent and indipendent variables
# 2) Homoscedasticity -- This assumption states that the variance of error terms are similar across the values of the independent variables
# 3) Multivariate Normality -- Multiple regression assumes that the residuals are normally distributed
# 4) Indipendence of Errors -- Residuals must distribute as Normal (Gaussian)
# 5) Lack of multicollinearity -- Multiple regression assumes that the independent variables are not highly correlated with each other


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir('C:\\Users\\niccolo\\Desktop\\DataScience101\\Part 2 - Regression\\Section 2.3 - Multiple Linear Regression')

# import dataset
dataset = pd.read_csv('./Data/50_Startups.csv')
x = dataset.iloc[:, :-1]
y = dataset.iloc[:, 4].values


# Encoding categorical Independent Variables
x = pd.concat([x, pd.get_dummies(x.State, drop_first=True)], axis=1)
x.drop('State', axis=1, inplace=True)
x = x.values


# Splitting Dataset into the training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size=0.2, random_state=0)


# Fitting Multiple Lineaar Regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
regressor.score(X_train, Y_train)

print('y = '+str(float(regressor.coef_[0]))+'x1 + '+str(float(regressor.coef_[1]))+'x2 + '+str(float(regressor.coef_[2]))+'x3 + '+str(float(regressor.coef_[3]))+'x4 + '+str(float(regressor.coef_[4]))+'x5 + '+str(regressor.intercept_))


# Predict Test Set
Y_pred = regressor.predict(X_test)
Delta_Salary = Y_test-Y_pred



########################
# Method 2
# Automatic p-value
########################
from statsmodels.api import OLS
def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        print(regressor_OLS.summary())
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    return x
# Paramter
SL = 0.05
X_opt = x[:, [0, 1, 2, 3, 4]]
X_Modeled = backwardElimination(X_opt, SL)



########################
# Method 3
# Automatic p-value and Adjusted R Squared Criterion
########################
from statsmodels.api import OLS
def backwardElimination(x, SL):
    numVars = len(x[0])
    temp = np.zeros((50,6)).astype(int)
    for i in range(0, numVars):
        regressor_OLS = OLS(y, x).fit()
        print(regressor_OLS.summary())
        maxVar = max(regressor_OLS.pvalues).astype(float)
        adjR_before = regressor_OLS.rsquared_adj.astype(float)
        if maxVar > SL:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:,j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = OLS(y, x).fit()
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)
                    if (adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:,[0,j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print (regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
        else: break
    return x
 
SL = 0.05
X_opt = x[:, [0, 1, 2, 3, 4]]
X_Modeled = backwardElimination(X_opt, SL)
