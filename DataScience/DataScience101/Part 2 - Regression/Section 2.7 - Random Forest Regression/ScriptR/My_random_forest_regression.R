# Decision Tree Regression Model
#install.packages('randomForest')
library(randomForest)

# set environment
setwd("C:/Users/nbenvenuti/Desktop/Tutorial PyR/Machine Learning/Part 2 - Regression/Section 2.7 - Random Forest Regression/")


# Importing the dataset
dataset = read.csv('./Data/Position_Salaries.csv')
dataset = dataset[2:3]


# # Splitting the dataset
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Profit, SplitRatio = 0.8)
# training_set = subset(dataset, split == T)
# test_set = subset(dataset, split == F)


# Fitting SVR to the dataset
set.seed(1234)
regressor = randomForest(x=dataset[1], y=dataset$Salary, ntree = 500)


# Prediction for 6.5 years of experience salary
y_pred=predict(regressor, data.frame(Level=6.5))



# Plotting Results Random Forest Regression
library(ggplot2)
ggplot() +
  geom_point(aes(x=dataset$Level, y=dataset$Salary), col="red") + 
  geom_line(aes(x=dataset$Level, y=predict(regressor)), col="blue")



# Plotting Results Random Forest Regression with high definition and smoother curve
x_grid=seq(min(dataset$Level), max(dataset$Level), by = 0.01)
ggplot() +
  geom_point(aes(x=dataset$Level, y=dataset$Salary), col="red") + 
  geom_line(aes(x=x_grid, y=predict(regressor, newdata = data.frame(Level = x_grid, Level2=x_grid^2, Level3=x_grid^3))), col="blue") + 
  ggtitle("Truth or Bluff (Random Forest Regression)") +
  xlab("Level") +
  ylab("Salary")