# Step 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# Step 2: Load dataset
data = pd.read_csv("insurance[1].csv")   # make sure path is correct
print(data.head())

# Step 3: Define features (X) and target (y)
X = data.drop('charges', axis=1)   # independent variables
y = data['charges']                # target variable

# Step 4: Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

# Step 5: Identify categorical and numerical columns
categorical_features = ['sex', 'smoker', 'region']
numerical_features = ['age', 'bmi', 'children']

# Step 6: Create preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('sta', StandardScaler(), numerical_features),  # standardize numerical data
        ('Oho', OneHotEncoder(), categorical_features)  # encode categorical data
    ]
)

print(preprocessor)

# Step 7: Create pipeline (preprocessing + model)
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Step 8: Fit model on training data
model.fit(X_train, y_train)

# Step 9: Predict on test data
y_pred = model.predict(X_test)

# Step 10: Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print(f"R² Score: {r2:.2f}")
print(f"Mean Absolute Error: {mae:.2f}")
