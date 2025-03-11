import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

#Reading the file
df = pd.read_csv('suv.csv')
# print(df.head())

#Selecting features and target variables
x = df[['Age', 'EstimatedSalary']]
y = df['Purchased']
# print(y.head())

#Spliting the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)

#Scaling the features
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#Selecting and training the decision tree (Entropy Criteian)
model = DecisionTreeClassifier(criterion='entropy', random_state=5)
model.fit(x_train, y_train)

#Predicting and evaluating the model
y_pred_entropy = model.predict(x_test)

confusion_entropy = confusion_matrix(y_test, y_pred_entropy)
class_report_entropy = classification_report(y_test, y_pred_entropy)

print(f"Consufion matrix (Entropy):\n{confusion_entropy}")
print(f"Classification report (Entropy):\n{class_report_entropy}")

#Selecting and training the decision tree (Gini Criterian)
model = DecisionTreeClassifier(criterion='gini', random_state=5)
model.fit(x_train, y_train)

#Predicting and evaluating the model
y_pred_gini = model.predict(x_test)

confusion_gini = confusion_matrix(y_test, y_pred_gini)
class_report_gini = classification_report(y_test, y_pred_gini)


print(f"Consufion matrix (gini):\n{confusion_gini}")
print(f"Classification report (gini):\n{class_report_gini}")

'''
Here, entropy produced 6 false positives, and 6 false negatives. Whereas, gini produced 6 false positives and 4 false negatives. From this it is seen that gini is better at identifying class 1.
In case of class 0, both the models have performed identically producing 6 false positives.

Overall gini has performed better as shown by 88% accuracy compared to that of Entropy's 85%.

Gini is more precise for negative (0) class and for class 1, it is slightly better than entropy (0.79 vs 0.78)
'''