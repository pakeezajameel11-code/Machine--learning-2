# student classification dataset
import pandas as pd
dataframe = pd.read_csv("data.csv", delimiter=";")
print(dataframe)
print(dataframe.head())
print(dataframe.describe())
print(dataframe.info())
print("datatype:", dataframe.dtypes)

print("nextrun:")
print(dataframe.isnull())
print(dataframe.isnull().sum()) # this for data cleaning # return no missing values in each column

# data manipulation
Y=dataframe['Target']
X=dataframe.drop("Target" , axis=1) # axis=1 is for column (header),, axis=0 is for rows
print("x:", X)
print("y:", Y)

# data split for training, testing
from sklearn.preprocessing import StandardScaler
scalar= StandardScaler()
scalar.fit(X) # fit analyze all the inputs columns 
x_scaled=scalar.transform(X.values)                # transform 

print("print x_scaled values:", x_scaled)

#training & testing data by split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_scaled, Y, train_size=0.7, random_state=23)
print(x_train)

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)

# predict y by x_test 
predict_y = log_reg.predict(x_test)
print(predict_y)

# matrix call to check accuraccy or find the difference btw actual/test y, and the predicted y,,
from sklearn.metrics import classification_report
result=classification_report(y_test, predict_y)
print(result)

from sklearn.metrics import confusion_matrix
result2 = confusion_matrix(y_test, predict_y)
print(result2)

# formuala to calculate accuraccy from confusion matrix
#formula = sum of all correct predicted values(diagonal values, TP+TN)/ sum of all the values that predicted false and true (TP+TN+FP+FN)
accuratepredicted = 320+77+627                      # diagonal values (TP+TN)
allpredictedvalues = 320+35+54+56+77+91+25+43+627       # (TP+TN+FP+FN)
Accuracy = accuratepredicted/allpredictedvalues
print(Accuracy)

precision = 320/320+35  #TP/TP+FP
print(precision)


recall = 320/320+56  #TP/TP+FN
print(recall)

# F1 SCORE
