from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model and scaler
model = joblib.load('maternAI_rf_model.pkl')
scaler = joblib.load('maternAI_scaler.pkl')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    try:
        features = [
            data['age'], data['systolicBP'], data['diastolicBP'], data['bloodSugar'],
            data['bodyTemp'], data['heartRate'], data['pregnancies'], data['complications'],
            data['hemoglobin'], data['bmi']
        ]

        # Reshape & scale
        features_scaled = scaler.transform([features])
        prediction = model.predict(features_scaled)[0]

        result = 'High Risk' if prediction == 1 else 'Low Risk'
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
