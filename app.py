from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from flask_cors import CORS
import numpy as np
import joblib

app = Flask(__name__)
print('app.py opened')

# Load the pre-trained model (make sure to replace this with your actual model file)
model = joblib.load('diabetes_model.pkl')  # Model trained using the Pima Indians Diabetes dataset

# Root route to show a welcome message
CORS(app, resources={r"/predict": {"origins": "*"}})

@app.route('/')
def home():
    return "Welcome to the Diabetes Prediction API. Use the /predict route to make predictions."
# Create the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:

        data = request.get_json()  # Get the input data from the frontend

        # Extract the values from the input
        age = float(data['age'])
        bmi = float(data['bmi'])
        glucose = float(data['glucose'])
        bloodPressure = float(data['bloodPressure'])
        pregnancies = float(data['pregnancies'])
        skinThickness = float(data['skinThickness'])
        insulin = float(data['insulin'])
        diabetesPedigreeFunction = float(data['diabetesPedigreeFunction'])
        input_data = np.array([[age, bmi, glucose, bloodPressure,pregnancies,skinThickness,insulin,diabetesPedigreeFunction]])
        prediction = model.predict(input_data)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)