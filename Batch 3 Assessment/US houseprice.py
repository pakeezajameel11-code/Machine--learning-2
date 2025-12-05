#
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

usd = pd.read_csv("US houuse price of 10 states.csv", sep=",")
print(usd.head())
print(usd.dtypes)
print(usd.isnull()) #Checks each value in the DataFrame usd and returns True if the value is NULL/NaN, otherwise False.
print(usd.isnull().sum()) #Count total missing values in each column


#fill missing values
usd.fillna({
    "house_size": usd["house_size"].mode()[0], # mode 0 is for index
    "bed": usd["bed"].mode()[0],  # numerical columns after cleaning, mean would be apply on these coloumns
    "bath": usd["bath"].mode()[0],
    "price": usd["price"].mode()[0],
    "broker": usd["broker"].mode()[0],
},inplace=True)

print(usd.isnull().sum())
print(usd.head())

# cleaning
# house_size
usd["house_size1"] = usd["house_size"].str.extract(r'(\d[\d,]*)')[0] \
                                        .str.replace(",", "") \
                                         .astype(int)
print("cleaned house_size col:", usd["house_size1"])
print(usd["house_size1"].head())
print(usd["house_size1"].dtype)



#bed & bath
usd["bed"] = usd["bed"].replace("Studio", "0")
usd["bed"] = usd["bed"].str.replace("bd", "")   
usd["bed"] = usd["bed"].astype(int) 
usd["bath"] = usd["bath"].replace("Studio", "0")
usd["bath"] = usd["bath"].str.replace("bd", "")       
usd["bath"] = usd["bath"].astype(int) 
print(usd["bed"])  
print(usd["bath"]) 

# price
usd["price1"] = usd["price"].str.replace("$", "", regex=False).str.replace(",", "", regex=False)
usd["price1"] = usd["price1"].astype(int)


# Seaborn
# line plot
usd_sorted = usd.sort_values("house_size1")
sns.lineplot(x="house_size1", y="price1", data=usd_sorted)
plt.title("House Size vs Price")
plt.show(block=True)

# scatter plot for uncleaned col
sns.scatterplot(x="house_size", y="price", data=usd)
plt.title("House Size vs Price")
plt.show(block=True)
# scatter plot for cleaned col 
sns.scatterplot(x="house_size1", y="price1", data=usd)
plt.title("House Size vs Price")
plt.show(block=True)


# features cleaned
x= usd[["house_size1", "bed", "bath"]]
y= usd["price1"]
print(x)
print(y)

# training & testing
xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=0.7, random_state=42)
print(xtrain)

#column transformer
num_col = ["house_size1", "bed", "bath"]
clc = ColumnTransformer(
    transformers=[
        ("scaling", StandardScaler(), num_col)], remainder="passthrough")

# Pipeline
# LogisticRegression
model1 = Pipeline(steps=[
    ("clc", clc),
    ("algorithm", LinearRegression())
])

model1.fit(xtrain, ytrain)
predictedy1 = model1.predict(xtest)
print("LR predictedy1:", predictedy1)

# randomforestclassifier
model2 = Pipeline(steps=[
    ("clc", clc),
    ("algorithm", RandomForestRegressor())
])

model2.fit(xtrain, ytrain)
predictedy2 = model2.predict(xtest)
print("RFR predictedy2:", predictedy2)

#GradientBoostingClassifier
model3 = Pipeline(steps=[
    ("clc", clc),
    ("algorithm", GradientBoostingRegressor())
])

model3.fit(xtrain, ytrain)
predictedy3 = model3.predict(xtest)
print(" GBR predictedy3:", predictedy3)

# Calculating scores
print("linear regressor mse:", mean_squared_error(predictedy1, ytest))
print("linear regressor m-abs:", mean_absolute_error(predictedy1, ytest))
print("linear regressor r2-score:", r2_score(predictedy1, ytest))

print("randomforest regressor mse:", mean_squared_error(predictedy2, ytest))
print("randomforest regressor m-abs:", mean_absolute_error(predictedy2, ytest))
print("randomforest regressor r2-score:", r2_score(predictedy2, ytest))

print("gradientboosting regressor mse:", mean_squared_error(predictedy3, ytest))
print("gradientboosting regressor m-abs:", mean_absolute_error(predictedy3, ytest))
print("gradientboosting regressor r2-score:", r2_score(predictedy3, ytest))










