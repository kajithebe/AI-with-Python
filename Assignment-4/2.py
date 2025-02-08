import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from sklearn.preprocessing import PolynomialFeatures
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

#Creating dataframe from csv file
df = pd.read_csv('weight-height.csv')

#Preparing the data
x = np.array(df[['weight']])
y = np.array(df['length'])


xMean = np.mean(x)
yMean = np.mean(y)

#Creating and training the model with training data
model = linear_model.LinearRegression()
model.fit(x, y)

#Predicting the weights using the model
yhat = model.predict(x)

#Plotting the data points and regression line
plt.scatter(x, y, label="Actual Data", alpha=.5)
plt.scatter(xMean, yMean, color='red')
plt.plot(x, yhat, color="blue")
plt.title("Scatter plot of height-weight")
plt.ylabel("Weight")
plt.xlabel("Height")
plt.show()

#Examining the quality of the model using RSME and R2
rmse = metrics.root_mean_squared_error(y, yhat)
r2 = metrics.r2_score(y, yhat)
print(f"RMSE: {rmse}, R2: {r2}")