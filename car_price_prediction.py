# car_price_prediction.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
df = pd.read_csv('car_data.csv')

# Preprocess the data
label_encoder = LabelEncoder()
df['brand'] = label_encoder.fit_transform(df['brand'])
df['model'] = label_encoder.fit_transform(df['model'])

# Select features and target variable
X = df[['brand', 'model', 'year', 'mileage', 'engine', 'power']]
y = df['price']

# Train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model and label encoders for future use
joblib.dump(model, 'car_price_model.pkl')
joblib.dump(label_encoder, 'brand_encoder.pkl')
joblib.dump(label_encoder, 'model_encoder.pkl')
