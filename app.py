import pandas as pd
from flask import Flask, render_template, request
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the car dataset
car_data = pd.read_csv('car_data.csv')

# Extract unique values for the dropdowns from the car data
brands = car_data['brand'].unique()
models = car_data['model'].unique()
years = car_data['year'].unique()
mileages = sorted(car_data['mileage'].unique())
engine_sizes = sorted(car_data['engine'].unique())
powers = sorted(car_data['power'].unique())

@app.route('/')
def home():
    return render_template('index.html', brands=brands, models=models, years=years, mileages=mileages, engine_sizes=engine_sizes, powers=powers)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    brand = request.form['brand']
    model = request.form['model']
    year = request.form['year']
    mileage = request.form['mileage']
    engine = request.form['engine']
    power = request.form['power']

    # Your prediction logic here (e.g., using a trained model)
    predicted_price = 20000  # Dummy value for example

    # Convert the predicted price to Indian Rupees
    predicted_price_inr = int(predicted_price * 82)  # Assuming 1 USD = 82 INR

    return render_template('index.html', predicted_price=predicted_price_inr, brands=brands, models=models, years=years, mileages=mileages, engine_sizes=engine_sizes, powers=powers)

if __name__ == '__main__':
    app.run(debug=True)
