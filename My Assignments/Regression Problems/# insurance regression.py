# insurance regression, categorical data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# insurance data , output column charges
df = pd.read_csv("insurance[1].csv")
print("insurance data:", df)

print(df.head())
print(df.describe())
print(df.shape)

# x, y 
x = df.drop("charges", axis=1)
y = df["charges"]
print(x)
print(y)

# splitting
xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=0.8, random_state=20)
print("x trained values:", xtrain)
print("y trained values:", ytrain)

# separate numerical & categorical data
numcol = ["age", "bmi", "children"]
catcol = ["sex", "smoker", "region"]

#columntransfer 2 in 1, numerical column's scaling, categorical column's encoding through onehotencoder
clt = ColumnTransformer(transformers=[
    ("numerical column", StandardScaler(), numcol),
    ("catcol", OneHotEncoder(), catcol)
])
print(clt)

# pipeline
model = Pipeline(steps=[
    ("columntransformer", clt),
    ("algorithm", GradientBoostingRegressor())
])

model.fit(xtrain, ytrain)
predicty = model.predict(xtest)
print("predicted y is:", predicty)

# applying evalution matrices
print(f" mean_abs_error is:,{mean_absolute_error(ytest, predicty)}")
print(f"mean_square_error is:, {mean_squared_error(ytest, predicty)}")
print(f"r2_score is:,{r2_score(ytest, predicty)}")