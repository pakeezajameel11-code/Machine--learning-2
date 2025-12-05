import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# load data
cd = pd.read_csv("used_cars_data.csv", sep=",")
print(cd.head())
print(cd.dtypes)
print(cd.isnull()) 
print(cd.isnull().sum())

#
print(cd["brand"].unique())
print(cd["model"].unique())
print(cd["location"].unique())
print(cd["engine"].unique())

# cleaning
# model
cd["model1"] = (cd["model"]
                .str.strip()
                .str.lower()
                .str.replace(r"[^a-z0-9 ]", "", regex=True))
print(cd["model1"])
print(cd["model1"].unique())

#fuel
cd["fuel1"] = (
    cd["fuel"]
        .str.strip()                                      # Remove spaces
        .str.lower()                                     # Convert to lowercase
        .str.replace(r"[^a-z0-9 ]", "", regex=True)      # Remove special characters((keep only letters, numbers, spaces))
        .replace({
            "diésel": "diesel",
            "gasolina": "gasoline",
            "electrico": "electric"
        })                                       # Standardize names
)
print(cd["fuel1"].unique())

# location
cd["location1"] = (
    cd["location"]
        .str.strip()                                # Remove extra spaces
        .str.replace(r"\d+", "", regex=True)       # remove numbers
        .str.replace(r"[^a-zA-Z0-9 ]", "", regex=True)  # remove symbols
        .str.lower()                               # optional: lowercase
)
print(cd["location1"].unique())

# engine
cd["engine1"] = (
    cd["engine"]
        .str.strip()                               # Remove spaces at start and end
        .str.lower()                               # Convert to lowercase
        .str.replace(r"[^a-z0-9 ]", "", regex=True) # Remove everything except letters, numbers, space
        .str.replace(r"\s+", " ", regex=True)       # Replace multiple spaces with a single space
)
print(cd["engine1"].unique())

#
x = cd.drop('price (eur)', axis=1)
y = cd['price (eur)']
print(x)
print(y)

# splitting
xtrain, xtest, ytrain, ytest = train_test_split(x,y, train_size=0.8, random_state=42)
print("xtrained is:", xtrain)
print("ytrained is:", ytrain)

# separate columns
num_col = ["year", "mileage (kms)"]
cat_cols = ["brand", "model1", "engine1", "fuel1", "gearbox", "location1"]

# column Trasnformer
clc = ColumnTransformer(transformers=[
    ('ohe', OneHotEncoder(drop='first', handle_unknown="ignore"), cat_cols),
    ('scaling', StandardScaler(), num_col),
])

# Pipeline
# linearRegression
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

# SVR
model4 = Pipeline(steps=[
    ("clc", clc),
    ("algorithm", SVR())
])

model4.fit(xtrain, ytrain)
predictedy4 = model4.predict(xtest)
print(" GBR predictedy3:", predictedy4)

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

print("SVR mse:", mean_squared_error(predictedy4, ytest))
print("SVR m-abs:", mean_absolute_error(predictedy4, ytest))
print("SVR r2-score:", r2_score(predictedy4, ytest))



