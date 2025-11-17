# fish regression
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import sklearn.ensemble 
import sklearn.metrics
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


# step 2
df = pd.read_csv("Fish[1].csv")
print(df)
print(df.head())
print(df.describe())
print(df.isnull())
print(df.isnull().sum())

# x, y

X = df.drop("Weight", axis=1) # tuple
Y = df["Weight"]
print(X)
print(Y)

# spliting
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, train_size=0.7, random_state=20)
print("xtrain values:", Xtrain)
print("ytrained values:", Ytrain)

# scaling 
from sklearn.preprocessing import StandardScaler, OneHotEncoder

numericalcol = ["Length1", "Length2", "Length3", "Height", "Width"]
encode = ["Species"]
clt = ColumnTransformer(
    transformers=[
    ("scale",StandardScaler(), numericalcol),
    ("encoding", OneHotEncoder(), encode)
    ]
 )
print(clt)

# pipeline 
from sklearn.ensemble import RandomForestRegressor

model = Pipeline(steps=[
    ("preprocessing", clt), 
    ("algorithm", RandomForestRegressor())
])

model.fit(Xtrain,Ytrain)
predictedy = model.predict(Xtest)
print(predictedy)

# 
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
print(f" the prediction according to abs error:{mean_absolute_error(Ytest, predictedy)}")
print(f" the prediction according to mse error:{mean_squared_error(Ytest, predictedy)}")
print(f" the prediction according to r2-score: {r2_score(Ytest, predictedy)}")