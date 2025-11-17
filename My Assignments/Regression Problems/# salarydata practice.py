# salarydata practice
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score

sdt = pd.read_csv('Salary_Data[1] (1).csv', sep=",")
print(sdt)

print(sdt.head())
print(sdt.describe())
print(sdt.shape)
print(sdt.isnull())
print(sdt.isnull().sum())

# filling missing values in data
sdt.fillna({'Age': sdt['Age'].mean(),
            'Gender': sdt['Gender'].mode()[0],
            'Education Level': sdt['Education Level'].mode()[0],
            'Job Title': sdt['Job Title'].mode()[0],
            'Years of Experience': sdt['Years of Experience'].mean(),
            'Salary' : sdt['Salary'].mean(),}, inplace=True)
print(sdt.isnull().sum())

# converting duplicate 
sdt['Education Level'] = sdt['Education Level'].str.lower().replace({
    "bechelor's degree" : "bechelor's",
    "master's degree" : "master's",
    "phd" : "phd"
})
print("it'll replace the duplicate values with assingened values:", sdt['Education Level'].unique())

# x, y
x = sdt.drop("Salary", axis=1)
y= sdt["Salary"]

# splitting
xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=0.8, random_state=42)
print(xtrain)
print(ytrain)

# seprate ordinal and nominal col
onehotencoding= ["Gender", "Job Title "]
ordinalencoding = ["Education Level "]
odecatclass = [['high school', "bechelor's", "master's", 'phd']]

# coluntransformer
clt = ColumnTransformer(transformers=[
    ('ode', OrdinalEncoder(categories=odecatclass, handle_unknown='use_encoded_value', unknown_value=-1), ordinalencoding),
    ('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), onehotencoding)
])
print(clt)
# pipeline
result = Pipeline(steps=[
    ('clt', clt),
    ('algorithm', GradientBoostingRegressor())
])
result.fit(xtrain, ytrain)
predictedy = result.predict(xtest)
print(predictedy)

# evaluation
print(f"mse:,{mean_squared_error(predictedy, ytest)}")
print(f"r2 score is:,{r2_score(predictedy,ytest)}")