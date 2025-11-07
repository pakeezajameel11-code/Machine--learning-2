# loan approval classification problem
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, precision_score, f1_score, recall_score

# data load
loan_data = pd.read_csv('loan_approval_dataset.csv', sep=',')
print(loan_data)

print(loan_data.head())
print(loan_data.describe())
print(loan_data.shape)
print(loan_data.isnull())
print(loan_data.isnull().sum())
print(loan_data.columns)

loan_data.columns=loan_data.columns.str.strip()
print(loan_data.head())
x = loan_data.drop('loan_status' , axis=1)
y = loan_data['loan_status']
print(x)
print(y)

from sklearn.preprocessing import LabelEncoder

# Encode target variable separately
le = LabelEncoder()
y = le.fit_transform(loan_data['loan_status'])

# splitting 
xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=0.7, random_state=42)
print("xtrained is:", xtrain)
print("ytrained is :", ytrain)

# seprate all numerical, categorical, target column, apply encoding on categorical column
num_col =loan_data.select_dtypes(include=['int64', 'Float64']).columns
onehot_col = ['education','self_employed']


# column transformer
clt = ColumnTransformer(transformers=[
    ('onehotencoding', OneHotEncoder(drop='first', handle_unknown='ignore'), onehot_col),
    ('scaling', StandardScaler(), num_col)
])
print(clt)

# pipeline
# logisticregression 
model1 = Pipeline(steps=[
    ('clt', clt),
    ('algorithm', LogisticRegression())
])

model1.fit(xtrain, ytrain)
predicty1 = model1.predict(xtest)
print("predictedy is:", predicty1)

# randomforest classifier
model2 = Pipeline(steps=[
    ('clt', clt),
    ('algorithm', RandomForestClassifier())
])

model2.fit(xtrain, ytrain)
predicty2 = model2.predict(xtest)
print("predictedy is:", predicty2)

# gradientboosting classifier 
model3 = Pipeline(steps=[
    ('clt', clt),
    ('algorithm', GradientBoostingClassifier())
])

model3.fit(xtrain, ytrain)
predicty3 = model3.predict(xtest)
print("predictedy is:", predicty3)

# classification report 
result1 = classification_report(ytest, predicty1)
print("logisticr regression:", result1)

result2 = classification_report(ytest, predicty2)
print("randomforest classifier:", result2)

result3 = classification_report(ytest, predicty3)
print('gardientboosting classifier:', result3)


#precision score
print("precision score for logistic regression")
print(precision_score(ytest, predicty1))

print("precision score for Random forest classfier")
print(precision_score(ytest,predicty2))

print("precision score for gradient booster classifier")
print(precision_score(ytest, predicty3))

#recall_score
print("recall_score for logistic regression")
print(recall_score(ytest, predicty1))

print("recall_score for Random forest classfier")
print(recall_score(ytest, predicty2 ))

print("recall_score for gradient booster classifier")
print(recall_score(ytest, predicty3))

#f1_score
print("f1_score for logistic regression")
print(f1_score(ytest, predicty1))

print("f1-score for Random forest classfier")
print(f1_score(ytest,predicty2))

print("f1-score for gradient booster classifier")
print(f1_score(ytest, predicty3))





