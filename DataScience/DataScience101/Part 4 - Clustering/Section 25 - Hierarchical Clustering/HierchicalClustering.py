# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:23:26 2020

@author: niccolo
"""

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir('C:\\Users\\niccolo\\Desktop\\DataScience101\\Part 4 - Clustering\\Section 24 - K-Means Clustering')


# Importing the dataset
dataset = pd.read_csv('.\Data\Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values


# Using Dendrogram method to find the optimal number of clusters
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title('Dendogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()


# Fitting Hierchical Clustering to the mall dataset
from sklearn.cluster import AgglomerativeClustering
HC = AgglomerativeClustering(n_clusters=5, 
                             affinity='euclidean',
                             linkage='ward')
y_HC = HC.fit_predict(X)



# Visualizing the CLusters ( s = size)
plt.scatter(X[y_HC == 0,0], X[y_HC == 0,1], s =100, c='red', label='Carefull')
plt.scatter(X[y_HC == 1,0], X[y_HC == 1,1], s =100, c='blue', label='Standard')
plt.scatter(X[y_HC == 2,0], X[y_HC == 2,1], s =100, c='green', label='Target')
plt.scatter(X[y_HC == 3,0], X[y_HC == 3,1], s =100, c='magenta', label='Careless')
plt.scatter(X[y_HC == 4,0], X[y_HC == 4,1], s =100, c='cyan', label='Sensible')
plt.title('Cluster of Clients')
plt.xlabel('Annual Income $')
plt.ylabel('Spending Score (1_100)')
plt.legend()
plt.show()


'''
Hierarchical clustering, as the name suggests is an algorithm that builds hierarchy of clusters. 
This algorithm starts with all the data points assigned to a cluster of their own. 
Then two nearest clusters are merged into the same cluster. In the end, this algorithm terminates when there is only a single cluster left.
'''