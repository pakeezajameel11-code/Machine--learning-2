# multivariate data 
import pandas as pd
df = pd.read_csv("gait.csv", delimiter=",")
print(df)

# analyzing data
print(df.head())
print(df.tail())
print(df.describe())
print(df.dtypes)
print("shape:", df.shape) 

print(df.isnull())
print(df.isnull().sum())

# manipulating data  #df['Total Doctors'] = df['Total Doctors'].str.replace(',', '').astype(int)
X = df.drop("angle", axis=1)
Y = df["angle"]
print(X)
print(Y)

# standardscalar
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
scaledx = scaler.transform(X.values)
print("x sacles values are:", scaledx)

#spliting training & testing
from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(scaledx, Y, train_size=0.8, random_state=20)
print("x trained values:", Xtrain)
print("y tained values:", Ytrain)

# linear model linear regression as target column has continuous float values not discrete values, so "regressor" is preffered
from sklearn.ensemble import RandomForestRegressor
logreg = RandomForestRegressor()
logreg.fit(Xtrain, Ytrain)
# predict y
predictedy = logreg.predict(Xtest)
print("predicted Y values are:", predictedy)

# classification report (for finding the error btw predicted values of y & actual/test y values )
#from sklearn.metrics import classification_report
#result = classification_report(Ytest, predictedy) 
#print(result)

# confusion matrix
#from sklearn.metrics import confusion_matrix
#result1 = confusion_matrix(Ytest, predictedy)
#print(result1)


#data type is cotinuous so classification models are unable to apply to find the accuracy apply regression model
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

mae = mean_absolute_error(Ytest, predictedy)
mse = mean_squared_error(Ytest, predictedy)
r2 = r2_score(Ytest, predictedy)

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R² Score:", r2)
