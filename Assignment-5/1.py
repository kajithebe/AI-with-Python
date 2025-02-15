import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, root_mean_squared_error
import seaborn as sns

matplotlib.use('TkAgg')

# Load the diabetes dataset as a DataFrame
data = load_diabetes(as_frame=True)
df = data['frame']

# Display correlation using heatmap
sns.heatmap(data=df.corr().round(2), annot=True)
plt.show()

# Select 'bmi' and 's5' as features and 'target' as the dependent variable
x_bmi_s5 = pd.DataFrame(df[['bmi', 's5']], columns=['bmi', 's5'])
y = df[['target']]

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_bmi_s5, y, test_size=0.2, random_state=5)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(x_train, y_train)

# Evaluate the model on training data
y_train_predict = model.predict(x_train)
rmse_train = root_mean_squared_error(y_train, y_train_predict)
r2_train = r2_score(y_train, y_train_predict)
print(f'RMSE (with bmi and s5 feature) - train: {rmse_train}')
print(f'R2 (with bmi and s5 feature) - train: {r2_train}')

# Evaluate the model on testing data
y_test_predict = model.predict(x_test)
rmse_test = root_mean_squared_error(y_test, y_test_predict)
r2_test = r2_score(y_test, y_test_predict)
print(f'RMSE (with bmi and s5 feature) - test: {rmse_test}')
print(f'R2 (with bmi and s5 feature) - test: {r2_test}')

'''
Since the model has already been trained using the features with the highest correlation to the target, namely 'bmi' and 's5', we will now include 'bp', which has the third highest correlation with the target (as seen on the heatmap).
'''

# Add 'bp' as an additional feature
x_bmi_s5_bp = pd.DataFrame(df[['bmi', 's5', 'bp']], columns=['bmi', 's5', 'bp'])
y = df[['target']]

# Split the dataset again with the new feature set
x_train, x_test, y_train, y_test = train_test_split(x_bmi_s5_bp, y, test_size=0.2, random_state=5)

# Retrain the model with the additional feature
model.fit(x_train, y_train)

# Evaluate the model with extended feature on training data
y_train_pred = model.predict(x_train)
rmse_train = root_mean_squared_error(y_train, y_train_pred)
r2_train = r2_score(y_train, y_train_pred)
print(f'RMSE (with bmi, s5, bp feature) - train: {rmse_train}')
print(f'R2 (with bmi, s5, bp feature) - train: {r2_train}')

# Evaluate the model with extended feature on testing data
y_test_pred = model.predict(x_test)
rmse_test = root_mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)
print(f'RMSE (with bmi, s5, bp feature) - test: {rmse_test}')
print(f'R2 (with bmi, s5, bp feature) - test: {r2_test}')

'''
Based on the RMSE and R² scores, the model with three features ('bmi', 's5', and 'bp') has a lower RMSE and a higher R² on both the training and testing data. This suggests a slight improvement with the addition of 'bp', though not a significant one. The relatively low R² scores indicate that the model does not perform well overall. Additionally, the high RMSE values suggest a considerable difference between the actual and predicted values. However, since there is no significant difference in RMSE between the training and testing data, the model does not exhibit overfitting.
'''

'''
From the heatmap, 's4' is the fourth most correlated feature with the target (0.43). If we were to add a fourth feature, it would be 's4'. However, since its correlation is weak (<0.5), adding it may not significantly enhance the model's performance. Additionally, it is crucial to assess the model for potential overfitting.
'''
