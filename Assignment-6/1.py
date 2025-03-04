import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

#Reading the csv file
df = pd.read_csv('bank.csv', delimiter=';')
print(df.head())

#Selecting columns for df2
df2= df[['y', 'job', 'marital', 'default', 'housing', 'poutcome']]
print(df2.head())

#Converting categorical variables to dummy numerical vallues
df3 = pd.get_dummies(df2,columns=['job','marital','default','housing','poutcome'])
print(df3.head())

#Converting 'y' column to numerical values
df3['y'] = df3['y'].map({'no': 0, 'yes': 1})
print(df3.head())

#Generating correlation headmap
sns.heatmap(df3.corr().round(2), annot=True, cmap='coolwarm')
plt.show()

#Defining variables x - explanatory and y - target
x = df3.drop(columns=['y'])
y = df3['y']

#Spliting dataset into training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=5)

#Initiate and train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

#Evaluating the logistic regression model
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
print(f"Confution matrix (logistic regression): \n{conf_matrix}")
print(f"Accuracy Score (logistic regression): \n{accuracy}")

#Initiating and training knn model
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(x_train, y_train)
y_pred_knn = knn_model.predict(x_test)

#Evaluating the knn model
conf_matrix_knn = confusion_matrix(y_test, y_pred_knn)
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f"Confution matrix (KNN): \n{conf_matrix_knn}")
print(f"Accuracy Score (KNN): \n{accuracy_knn}")

'''
Comparing the results:
- Accuracy score of logistic regression is 0.8974358974358975 and that of knn is 0.8735632183908046. It means the logistic regression is more accurate.

- The logistic regression has less false positives (9) compared to that of knn (28). It means that logistic regression makes fewer incorrect predications of "Yes" when the actual value is "No".

- The false negatives in also lower in case of logistic regression (107) compared to that of knn (115). It means the logistic regression makes fewer incorrect predictions of "No" when the actual value is "Yes".
'''