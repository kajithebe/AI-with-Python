import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report

#Load the dataset
df = pd.read_csv('data_banknote_authentication.csv')
# print(df.head())

#Defining the features and target variable
x = df.iloc[:, 0:-1]
y=df['class']
# print(y.head())

#Spliting the data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=20)

#Initiating the linear svc model and training it
model = SVC(kernel='linear')
model.fit(x_train, y_train)

#Predicting the target variable based on test features
y_pred = model.predict(x_test)

#Computing and printing confusion matrix and classification report
confusion = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Confusion matrix (linear):\n{confusion}")
print(f"Classification report (linear):\n{class_report}")

#Initiating the RBF svc model and training it
model = SVC(kernel='rbf')
model.fit(x_train, y_train)

#Predicting the target variable based on test features
y_pred_rbf = model.predict(x_test)

#Computing and printing confusion matrix and classification report
confusion_rbf = confusion_matrix(y_test, y_pred_rbf)
class_report_rbf = classification_report(y_test, y_pred_rbf)

print(f"Confusion matrix (rbf):\n{confusion_rbf}")
print(f"Classification report (rbf):\n{class_report_rbf}")

'''
Based on the results, both models performed excceptionally well. However, there are tiny differences:
- Linear karnel produced 2 false positives resulting in 99% accuracy. Precision, recall, and f1-score are very high but not perfect.
- RBF didn't misclassified any data; meaning there's no false results. Hence, the accuracy is 100%. recision, recall, and f1-score all are perfect.

Linear kernel assumes that the data is linearly separable. It performed very well, but a small number of data were incorrectly classified (2 FP).

RBF kernel is more flexible and can model complex, nonlinear decision boundries. In the above case, it perfectly classified all the data (no false results); meaning, it outperformed the linear model.

Since RBF model generated 100% accuracy, it suggests that a nonlinear decision boundry is optimal for this dataset.
'''
