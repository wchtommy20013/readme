# Hierchical Clustering

setwd("C:\\Users/nbenvenuti/Desktop/Tutorial PyR/Machine Learning/Part 4 - Clustering/Section 24 - K-Means Clustering/")

# Importing the dataset
dataset = read.csv('./Data/Mall_Customers.csv')
X <- dataset[4:5]

# Using Dendrogram method to find the optimal number of clusters
Dendrogram = hclust(dist(X, method = 'euclidean'), method='ward.D')
plot(Dendrogram, 
     main= 'Dendrogram',
     xlab='Euclidean Distance',
     ylab='Customers')



# Fitting Hierchical Clustering to the mall dataset
hc = hclust(dist(X, method = 'euclidean'), method='ward.D')
y_hc = cutree(hc, 5)


# Visualizing the CLusters ( s = size)
library(cluster)
clusplot(X, y_hc, 
         lines = 0, shade=TRUE, color=TRUE, label=2, plotchar = FALSE,
         main="Cluster of Clients", xlab="Annual Income", ylab="Spending Score")