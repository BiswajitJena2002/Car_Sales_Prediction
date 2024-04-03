from flask import Flask, request, render_template
import numpy as np
import joblib

# Flask app
app = Flask(__name__)

# Load the pre-trained model and the fitted scaler
loaded_model = joblib.load('Car_Sales_rf.joblib')
scaler = joblib.load('Car_Sales_scaler.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input values from the form
        year = float(request.form['year'])
        make = float(request.form['make'])
        transmission = float(request.form['transmission'])
        state = float(request.form['state'])
        condition = float(request.form['condition'])
        odometer = float(request.form['odometer'])
        color = float(request.form['color'])
        interior = float(request.form['interior'])

        # Organize the input features as a numpy array
        features = np.array([[year,make,transmission,state,condition,odometer,color,interior]])

        # Scale the input data using the fitted scaler
        scaled_test_data = scaler.transform(features)

        # Make prediction using the pre-trained model
        prediction = loaded_model.predict(scaled_test_data)

        return render_template('index.html', prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)