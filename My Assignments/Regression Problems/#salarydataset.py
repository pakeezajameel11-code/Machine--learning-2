import pandas as pd
import sklearn.model_selection
import sklearn.preprocessing
import sklearn.compose
import sklearn.pipeline
import sklearn.metrics

Salarydata=pd.read_csv('Encoding techniques\Salary_Data[1].csv', sep=",")
print("This will print all the dataset:", Salarydata)

print('This will print information of dataset',Salarydata.info)

print('This will give statistic operations:', Salarydata.describe())

print("This will confirm if dataset contain any null value:", Salarydata.isnull())

print("This will return how many null values are there in each column:",Salarydata.isnull().sum())

#Salarydata['Gender'].fillna(Salarydata['Gender'].mode()[0], inplace=True)

#print(Salarydata.head(176))

#print(Salarydata['Gender'].isnull().sum())

#Cleaning data by filling missing values in dataframe
Salarydata.fillna({
    'Age': Salarydata['Age'].mean(),
    'Gender': Salarydata['Gender'].mode()[0],
    'Education Level': Salarydata['Education Level'].mode()[0],
    'Job Title': Salarydata['Job Title'].mode()[0],
    'Years of Experience': Salarydata['Years of Experience'].mean(),
    'Salary': Salarydata['Salary'].mean()
}, inplace=True)

print(Salarydata.isnull().sum())

print("Return uniques values in Educational Column:", Salarydata['Education Level'].unique())
#Cleaning data by removing duplicacy (e.g replace all "bachelor's degree" with "bachelor's")
Salarydata['Education Level'] = Salarydata['Education Level'].str.lower().replace({
    "bachelor's degree": "bachelor's",
    "master's degree": "master's",
    "phd": "phd"
})
print("Return uniques values in Educational Column:", Salarydata['Education Level'].unique())


X=Salarydata.drop("Salary", axis=1)
Y=Salarydata['Salary']

print("Our input columns are;", X)
print("Our output Columns are:", Y)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X, Y, train_size=0.7, random_state=23)
print("Our train data is:", X_train)

Ordinal_columns=['Education Level']
ordinal_categories=[['high school',"bachelor's" ,"master's", 'phd'] ]
nominal_columns=['Gender','Job Title']

from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer

preprocessing=ColumnTransformer(transformers=[
    ('ordinal',OrdinalEncoder(categories=ordinal_categories,handle_unknown='use_encoded_value', unknown_value=-1),  Ordinal_columns),
    ('Ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), nominal_columns)
])

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
model=Pipeline(steps=[
    ("preprocessing", preprocessing),
    ("algorithms", GradientBoostingRegressor())
])

model.fit(X_train, Y_train)
pred_Y=model.predict(X_test)


from sklearn.metrics import  r2_score,mean_absolute_error
print("Result for R_2 score:", r2_score(Y_test,pred_Y))
print("next run")
print("Result for mean absoulte error:", mean_absolute_error(Y_test, pred_Y))


