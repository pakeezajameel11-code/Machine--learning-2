# advertising data regression , prdicting sales
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('advertising.csv', delimiter=',')
print(df)
# analyzing data
print(df.head())
print("dataframe shape:", df.shape)
print("aggregate/stats values:", df.describe())
print("correlation:", df.corr())
print("datatype is:", df.dtypes)

print("null values in data:", df.isnull())
print("missing values:", df.isnull().sum())

# manipulating data define dep/indep varaible
# .reshape() to covert data from 1d to  2d array 
X = df[['TV', 'Radio', 'Newspaper']] # double brackets to pick / select them form dataframe:
Y = df['Sales']

print(X)
print("x shape:", X.shape)
print("target variable:", Y)

# scaling by standard scaler
from sklearn.preprocessing import StandardScaler
scaled = StandardScaler()
scaled.fit(X)
scaledx = scaled.transform(X.values)
print("x scaled values are:", scaledx)

# splitting x and y # for varaibles
from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(scaledx, Y, train_size=0.7, random_state=20)
print("x trained values are:", Xtrain)
print("y trained values are:", Ytrain)
print('Xtest values are:', Xtest)
print("y test values are:", Ytest)

# Model selection , Multiple linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(Xtrain, Ytrain)
predictedy = regressor.predict(Xtest)
print("predictedy values:", predictedy)

# after model selection and predictey , we can check intercept 
#intercept means if x=0 than how much change it in values of y
# the predicted value of the dependent variable when all independent variables are zero.
print("regression intercept:",regressor.intercept_ )
# and the coefficients of features, relationship between one independent variable and a dependent variable,
#It tells how much the dependent variable is predicted to change for a one-unit increase in the independent variable.
print("regression coefficient:", regressor.coef_)

#We use this code to see how much each independent variable (feature) affects the target (dependent variable) in a multiple linear regression model.

result= pd.DataFrame({"Actual": Ytest, "Predicted": predictedy})
print(result)

#final step is to evaluate the performance of our multiple linear regression
# now calculate mean absolute error (MAE), mean squared error (MSE), Root mean squarred error (RMSE) 
# to understand if our predicted values are too far from our actual values,
from sklearn.metrics import mean_absolute_error, mean_squared_error
MAE = mean_absolute_error(Ytest, predictedy)
MSE = mean_squared_error(Ytest, predictedy)
RMSE = np.sqrt(MSE)

print(f'mean absolute error: {MAE:.2f}')
print(f'Mean squared error: {MSE:.2f}')
print(f'Root mean squared error: {RMSE:.2f}')





