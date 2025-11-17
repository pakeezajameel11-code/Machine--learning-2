# heart disease data (encoding/ensemble techniques)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
#from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix

# data load
hdt = pd.read_csv('heart-2.csv', sep=',')
print(hdt)

# analyze
print(hdt.head())
print(hdt.describe())
print(hdt.shape)
print(hdt.isnull())
print(hdt.isnull().sum())
#print(hdt.unique())

# x,y
x = hdt.drop('target', axis=1)
y = hdt['target']
print(x)
print(y)

# splitting
xtrain, xtest, ytrain, ytest = train_test_split(x,y, train_size=0.7, random_state=42)
print("xtrained is:", xtrain)
print("ytrained is:", ytrain)

# seprate columns
numcol = ['age','trestbps', 'chol', 'thalach', 'oldpeak', 'ca']
ordinalencoding = ['cp', 'slope']
onehotencoding = ['restecg', 'thal']
binarycol = ['sex', 'fbs', 'exang']

# column trasformer
clt = ColumnTransformer(transformers=[
    ('ode', OrdinalEncoder(), ordinalencoding),
    ('ohe', OneHotEncoder(drop='first'), onehotencoding),
    ('scaling', StandardScaler(), numcol),
    ('binary', 'passthrough',  binarycol)
])

# pipeline
model = Pipeline(steps=[
    ('clt', clt),
    ('algorithm', GradientBoostingClassifier())  
])
model.fit(xtrain, ytrain)
predicty = model.predict(xtest)
print("predictedy is :", predicty)

# calssification report
result = classification_report(ytest,predicty)
print(result)

result1 = confusion_matrix(ytest, predicty)
print(result1)