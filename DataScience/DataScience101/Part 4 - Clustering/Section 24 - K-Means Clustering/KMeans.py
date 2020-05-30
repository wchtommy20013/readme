# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:19:59 2020

@author: niccolo
"""

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir('C:\\Users\\niccolo\\Desktop\\DataScience101\\Part 4 - Clustering\\Section 24 - K-Means Clustering')
#https://en.wikipedia.org/wiki/K-means_clustering

# Importing the dataset
dataset = pd.read_csv('.\Data\Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values


# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range (1,11):
    kmeans = KMeans(n_clusters=i, 
                    init='k-means++', # or random
                    max_iter=300, 
                    n_init=10,
                    random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of CLusters')
plt.ylabel('WCSS')
plt.show()


# Applying k-means to the mall dataset
kmeans = KMeans(n_clusters=5, init='k-means++', 
                    max_iter=300, 
                    n_init=10,
                    random_state=0)
y_kmeans = kmeans.fit_predict(X)


# Visualizing the CLusters ( s = size)
plt.scatter(X[y_kmeans == 0,0], X[y_kmeans == 0,1], s =100, c='red', label='Carefull')
plt.scatter(X[y_kmeans == 1,0], X[y_kmeans == 1,1], s =100, c='blue', label='Standard')
plt.scatter(X[y_kmeans == 2,0], X[y_kmeans == 2,1], s =100, c='green', label='Target')
plt.scatter(X[y_kmeans == 3,0], X[y_kmeans == 3,1], s =100, c='magenta', label='Careless')
plt.scatter(X[y_kmeans == 4,0], X[y_kmeans == 4,1], s =100, c='cyan', label='Sensible')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1], s=300, c='yellow', label='Centroids')
plt.title('Cluster of Clients')
plt.xlabel('Annual Income $')
plt.ylabel('Spending Score (1_100)')
plt.legend()
plt.show()


'''
K means is an iterative clustering algorithm that aims to find local maxima in each iteration. This algorithm works in these 5 steps :
    Specify the desired number of clusters K
    Randomly assign each data point to a cluster 
    Compute cluster centroids 
    Re-assign each point to the closest cluster centroid
    Re-compute cluster centroids 
'''
