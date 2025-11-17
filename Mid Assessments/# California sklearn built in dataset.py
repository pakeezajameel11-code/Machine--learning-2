# California sklearn built in dataset
import pandas as pd 
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

#fetch california data
californiahousing = fetch_california_housing()
# california features 
californiadata = pd.DataFrame(californiahousing.data, columns=californiahousing.feature_names)
# target column define
californiadata['MEDV'] = californiahousing.target

print(californiadata)
print(californiadata.head(15))
x = californiadata.drop('MEDV', axis=1)
y = californiadata['MEDV'] # target column print
print(y)

# training testin splitting
xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=0.8, random_state=42)
print(xtrain)

rfr = RandomForestRegressor(n_estimators=100, random_state=42)
rfr.fit(xtrain, ytrain)
predicty = rfr.predict(xtest)
print(predicty)

svr = SVR()
svr.fit(xtrain, ytrain)
predicty2 = svr.predict(xtest)
print(predicty2)

gbr= GradientBoostingRegressor(n_estimators=100, random_state=42)
gbr.fit(xtrain, ytrain)
predicty1 = gbr.predict(xtest)
print('gbr presictedy is:', predicty1)

print("randomforest regressor:", mean_squared_error(predicty, ytest))
print("randomforest regressor:", r2_score(predicty, ytest))

print("svr:", mean_squared_error(predicty2, ytest))
print("svr:", r2_score(predicty2, ytest))

print("gradientboosting regressor:", mean_squared_error(predicty1, ytest))
print("gradientboosting regressor:", r2_score(predicty1, ytest))



