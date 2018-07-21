# Estimate Mean and Variance

# Calculate the mean value of a list of numbers

# Calculate root mean squared error
from math import sqrt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
predictedglobal=[]
def rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return sqrt(mean_error)

# Evaluate regression algorithm on training dataset
def evaluate_algorithm(dataset, algorithm):
	test_set = list()
	for row in dataset:
		row_copy = list(row)
		row_copy[-1] = None
		test_set.append(row_copy)
	predicted = algorithm(dataset, test_set)
	print(predicted)
	actual = [row[-1] for row in dataset]
	rmse = rmse_metric(actual, predicted)
	return rmse,predicted


def mean(values):
	return sum(values) / float(len(values))

# Calculate the variance of a list of numbers
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])

# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar

# Calculate coefficients
def coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean, y_mean = mean(x), mean(y)
	b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
	b0 = y_mean - b1 * x_mean
	return [b0, b1]

def simple_linear_regression(train, test):
	predictions = list()
	b0, b1 = coefficients(train)
	for row in test:
		yhat = b0 + b1 * row[0]
		predictions.append(yhat)
	return predictions

# calculate mean and variance
#dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
df1 = pd.read_excel('d:/report/Linear.xls', na_values=['NA'])
x1=df1.loc[:,'x']
y1=df1.loc[:,'y']
#print("valiues of X & Y")
x=list(x1)
y=list(y1)
dataset=np.vstack((x,y)).T
print(dataset)

#x = [row[0] for row in dataset]
#y = [row[1] for row in dataset]
mean_x, mean_y = mean(x), mean(y)
var_x, var_y = variance(x, mean_x), variance(y, mean_y)
covar = covariance(x, mean_x, y, mean_y)
b0, b1 = coefficients(dataset)

rmse,predictedglobal = evaluate_algorithm(dataset, simple_linear_regression)

print("predictedglobal")
print(predictedglobal)
print('RMSE: %.3f' % (rmse))

print('Coefficients: B0=%.3f, B1=%.3f' % (b0, b1))
print('Covariance: %.3f' % (covar))

print('x stats: mean=%.3f variance=%.3f' % (mean_x, var_x))
print('y stats: mean=%.3f variance=%.3f' % (mean_y, var_y))

plt.scatter(x=x,y=y,alpha = 0.8)
plt.scatter(x=x,y=predictedglobal, alpha = 0.8)
plt.xlabel("x")
plt.ylabel("x")
plt.title("Linear Regression")
plt.show()