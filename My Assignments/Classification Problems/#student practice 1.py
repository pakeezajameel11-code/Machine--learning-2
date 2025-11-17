#student practice 1
import pandas as pd
df = pd.read_csv('data.csv', delimiter=';')
print(df)

# analyzing data
print(df.head())
print(df.tail())
print(df.describe())
print("data info:" , df.info())
print("data types:", df.dtypes)

print("missing values:", df.isnull())
print("sum:", df.isnull().sum()) #

#Data Manipulation X, Y 
X = df.drop("Target", axis=1)
Y = df["Target"]

print("x values:", X)
print("y column:", Y)

# scaling data for training and testing
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
scalar.fit(X)
sacaled_x = scalar.transform(X.values)
print("x scaled values:", sacaled_x)

# spliting scaled data
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(sacaled_x, Y, train_size=0.7, random_state=20)
print(" x trained values are:", X_train)
print("x test values:", X_test)
print("y trained values:", Y_train)

#model selection 
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
# predicted y by xtest
predicty = logreg.predict(X_test)
print(predicty)

# classification model
from sklearn.metrics import classification_report
result= classification_report(Y_test, predicty)
print(result)

# confusion matrix 
from sklearn.metrics import confusion_matrix
result1 = confusion_matrix(Y_test, predicty)
print(result1)

#




