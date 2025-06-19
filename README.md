# 📈 Stock Trend Detector using LSTM

A deep learning-based project that predicts stock price trends using historical data and a Long Short-Term Memory (LSTM) neural network.

## 🧠 Overview

This project fetches historical stock price data using the `yFinance` API, preprocesses it, and trains an LSTM neural network to predict future stock price trends. The model is trained on the closing prices and visualizes the difference between actual and predicted prices.

## 🚀 Features

- 📊 Fetch real-time historical data for any stock symbol  
- 🔄 Normalize and preprocess time-series data  
- 🧠 Build and train an LSTM neural network  
- 🧪 Predict stock prices using deep learning  
- 📉 Visualize actual vs predicted stock prices  

## 🔧 Technologies Used

- Python 🐍  
- yFinance 📈  
- NumPy  
- scikit-learn  
- TensorFlow / Keras 🧠  
- Matplotlib 📊  

## Skills Demonstrated
- Time series forecasting
- Deep learning with LSTM
- Real-world data handling
- AI model evaluation and visualization


## 🛠 Project Structure
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

## 🖥️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/V-Varna/stock_trend_detector_LSTM.git
cd stock_trend_detector_LSTM
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Project
bash
Copy
Edit
python main.py

🌟 Example Output
Here’s a sample of the result (actual vs predicted prices):
![Screenshot 2025-06-20 013103](https://github.com/user-attachments/assets/76c4b2b7-d609-46f1-b727-eb52cb6205a0)

🙌 Contributing
If you find issues or want to contribute new features, feel free to fork the repo and submit a pull request!

📝 License
This project is open source and available under the MIT License.

