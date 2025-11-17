# salarydata regression (encoding techniques)

import pandas as pd
from sklearn.preprocessing  import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# sdt = salarydata
sdt = pd.read_csv("Salary_Data[1] (1).csv", delimiter=',')
print(sdt)

print("salary data head:", sdt.head())
print("salary data describe:", sdt.describe())
print("salary data info:", sdt.info)
print("salary data type:", sdt.dtypes)
print("salary data shape:", sdt.shape)
print("salary data missing values :", sdt.isnull())
print("salary data how many missing values in each column :", sdt.isnull().sum()) 

# fill missing values in one column 
# for 1 column Gender
sdt['Gender'].fillna(sdt['Gender'].mode()[0], inplace=True)
print(sdt.head(176))

# for filling all the missing values in data
sdt.fillna({
    'Age': sdt['Age'].mean(),
    'Gender': sdt['Gender'].mode()[0],
    'Education Level': sdt['Education Level'].mode()[0],
    'Job Title': sdt['Job Title'].mode()[0],
    'Years of Experience': sdt['Years of Experience'].mean(),
    'Salary': sdt['Salary'].mean(), 
}, inplace=True)

print(sdt.isnull().sum())

#check duplicate values in education column
print("return unique values in educationalcolumn:", sdt['Education Level'].unique())
# cleaning duplicate values in education level column
sdt['Education Level'] = sdt['Education Level'].str.lower().replace({
    "bachelor's degree": "bachelor's",
    "master's degree": "master's",
    "phd": "phd"
})
print("it returns unique values in educationalColumn:", sdt['Education Level'].unique())

# x, y
x  = sdt.drop("Salary", axis=1)
y= sdt["Salary"]
print(x)
print(y)

# splitting data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=0.7, random_state=40)
print("x trained values are:", xtrain)
print("y trained values are:" , ytrain)

# seprate numerical and categorical columns for columntransformer 
# we apply only encoding methods in columntransformer (no standardscaling in this data)

ordinalencoding = ['Education Level']
ordinalcategoriescalsses = [['high school', "bechelor's", "master's", "phd" ]]
onehotencoding = ['Gender', 'Job Title']

clt = ColumnTransformer(transformers=[
    ('ODE', OrdinalEncoder(categories= ordinalcategoriescalsses, handle_unknown='use_encoded_value', unknown_value= -1 ), ordinalencoding),
    ('OHE', OneHotEncoder(sparse_output=False, handle_unknown= 'ignore'), onehotencoding)
])
print(clt)

# pipelines
model = Pipeline(steps=[
    ('clt', clt),
    ('algorthim', GradientBoostingRegressor())
])

# training testing predicting
model.fit(xtrain, ytrain)
predictedy = model.predict(xtest)
print("predictedy is:", predictedy)

# evaluation 
print(f"mean absolute error:, {mean_absolute_error(ytest, predictedy)}")
print(f'mean squarred error:, {mean_squared_error(ytest, predictedy)}')
print(f' r2 sore is:, {r2_score(ytest, predictedy)}')