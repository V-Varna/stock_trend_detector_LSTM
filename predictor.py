"""
predictor.py
Handles prediction and inverse transformation.
"""
import numpy as np

def predict_and_inverse(model, X_test, scaler):
    predictions = model.predict(X_test)
    predictions = scaler.inverse_transform(predictions)
    return predictions
