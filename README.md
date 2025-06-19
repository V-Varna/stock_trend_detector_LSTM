# Stock Price Trend Predictor using LSTM (AI + Finance)

## Overview
This project predicts future stock prices using historical data and an AI technique called LSTM (Long Short-Term Memory), a type of neural network suited for time-series forecasting.

## Key Features
- Fetches real-time stock data using yfinance
- Processes and normalizes data for AI input
- Trains an LSTM model to understand price patterns
- Visualizes real vs predicted prices using matplotlib

## Tech Stack
- Python
- TensorFlow/Keras
- yFinance
- NumPy
- Matplotlib
- Scikit-learn

## Skills Demonstrated
- Time series forecasting
- Deep learning with LSTM
- Real-world data handling
- AI model evaluation and visualization

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run the pipeline: `python main.py`

## File Structure
```
stock_predictor/
├── data_loader.py         # handles data downloading
├── preprocessing.py       # handles normalization & sequences
├── model.py               # builds and trains the model
├── predictor.py           # predicts and inverse transforms
├── visualize.py           # handles all plots
├── main.py                # runs the full pipeline
└── README.md              # explains your project
```
