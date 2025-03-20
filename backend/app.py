from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from model import load_model, predict,ANN_Model

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with the backend

# Load the model
model = load_model()

@app.route('/')
def home():
    return "Diabetes Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict_diabetes():
    try:
        # Get input data from JSON request
        data = request.json['features']
        prediction = predict(model, data)

        return jsonify({'prediction': "Diabetic" if prediction == 1 else "Non-Diabetic"})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
