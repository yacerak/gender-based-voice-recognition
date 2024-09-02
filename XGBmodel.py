import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from xgboost import XGBClassifier, DMatrix
from sklearn.preprocessing import LabelEncoder


voices = pd.read_csv("voice.csv")
# Drop irrelevant columns
X = voices.drop(columns=["label"])

# Target variable
y = voices["label"]

# Convert labels to numerical format using LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate the imputer (replace NaN values with the mean of the column)
imputer = SimpleImputer(strategy='mean')

# Fit and transform the imputer on the training data
X_train_imputed = imputer.fit_transform(X_train)

# Transform the test data using the imputer
X_test_imputed = imputer.transform(X_test)

# Instantiate the XGBoost model
xgb_model = XGBClassifier()

# Train the model using the imputed data
xgb_model.fit(X_train_imputed, y_train)

# Predictions on the test set
y_pred = xgb_model.predict(X_test_imputed)

def xgb_predict(features):
    features_imputed = imputer.transform(features)

    gender_probabilities = xgb_model.predict_proba(features_imputed)

    probabilities_for_female = gender_probabilities[:, 0]
    probabilities_for_male = gender_probabilities[:, 1]

    if probabilities_for_female >= 0.92:
        prediction = "Female"
    else:
        prediction = "Male"
    return prediction

