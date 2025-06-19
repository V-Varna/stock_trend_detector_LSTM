"""
main.py
Runs the full pipeline: data loading, preprocessing, training, prediction, and visualization.
"""
from data_loader import download_stock_data
from preprocessing import normalize_data, create_sequences
from model import build_lstm_model, train_model
from predictor import predict_and_inverse
from visualize import plot_predictions
import numpy as np

# Parameters
ticker = 'AAPL'
start_date = '2018-01-01'
end_date = '2023-01-01'
seq_length = 60

data = download_stock_data(ticker, start_date, end_date)
close_prices = data['Close'].values.reshape(-1, 1)

scaled_data, scaler = normalize_data(close_prices)
X, y = create_sequences(scaled_data, seq_length)

split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

model = build_lstm_model((X_train.shape[1], 1))
history = train_model(model, X_train, y_train)

predictions = predict_and_inverse(model, X_test, scaler)
real = scaler.inverse_transform(y_test.reshape(-1, 1))

plot_predictions(real, predictions)
