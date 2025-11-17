# student practice 2
import pandas as pd
df = pd.read_csv("data.csv", delimiter=";")
print(df)

# analysis methods
print(df.head())
print(df.tail())
print(df.describe())
print(df.dtypes)
# for finding missing values in data
print(df.isnull())
print(df.isnull().sum())

# manipulating data, x,y columns define
X = df.drop("Target", axis=1)
Y = df["Target"]
print(X)
print(Y)

#scaling data for training and testing
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
scaledx = scaler.transform(X.values)
print(scaledx)

# spliting data into four variables train & test
from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(scaledx, Y, train_size=0.7, random_state=20)
print("x traiend values are:", Xtrain)
print("y tarained values are:", Ytrain)

# linear model selection logistic regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(Xtrain, Ytrain)

predictedy = logreg.predict(X)
print(predictedy)

# classification report
from sklearn.metrics import classification_report
result = classification_report(Ytest, predictedy)
print(result)

# confusion matrix
from sklearn.metrics import confusion_matrix
result1 = confusion_matrix(Ytest, predictedy)
print(result1)