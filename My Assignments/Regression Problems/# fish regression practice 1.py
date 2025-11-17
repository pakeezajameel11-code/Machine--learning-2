# fish regression practice 1
# import everything which you need for your data manipulation
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline 
from sklearn.ensemble import RandomForestRegressor
import sklearn.metrics 

# print data (give relative path of file)
fdf = pd.read_csv("Fish[1].csv")
print("fish data:", fdf )

# analyzing data
print(fdf.head())
print(fdf.describe())
#print(fdf.dtypes)
#print("fish data shape:", fdf.shape)
print(fdf.isnull())
print(fdf.isnull().sum())

# x,y    where  x input columns, y output target column
x = fdf.drop("Weight", axis=1)
y = fdf["Weight"]
print(x)
print("y column:", y)

# training & testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=0.7, random_state=40)
print("x trained:", xtrain)
print("x tested values:", xtest)
print("y trained values:", ytrain)

#separate (numerical) and categorical column for encoding method, here "species" is an input column, to encode it we use OneHotEncoder
numfeature = ["Length1", "Length2", "Length3", "Height", "Width"]
catcol = ["Species"]
# we use columntrasformer to apply encoding and standardscalar in one step(concisely)
cltr = ColumnTransformer(
    transformers=[
    ('scale',StandardScaler(), numfeature),
    ('catcol', OneHotEncoder(), catcol)
])
print(cltr)

# pipelines concept we can apply 
model = Pipeline(steps=[
    ("cltr", cltr),
    ("algorithm", RandomForestRegressor())
])

model.fit(xtrain, ytrain)
predicty = model.predict(xtest)
print(" predicted y is:", predicty)

# import evalutionmatrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
print(f"absolute mean error is:,{mean_absolute_error(ytest, predicty)}")
print(f" mean squarred error is:,{mean_squared_error(ytest, predicty)}")
print(f" r2 score is:, {r2_score(ytest, predicty)}")