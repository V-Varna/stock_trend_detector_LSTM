"""
visualize.py
Handles all plots for real vs predicted prices.
"""
import matplotlib.pyplot as plt

def plot_predictions(real, predicted, title='Stock Price Prediction'):
    plt.figure(figsize=(10,6))
    plt.plot(real, color='blue', label='Actual Price')
    plt.plot(predicted, color='red', label='Predicted Price')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
