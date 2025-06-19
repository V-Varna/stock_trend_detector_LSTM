"""
data_loader.py
Handles downloading historical stock data using yfinance.
"""

import yfinance as yf
import pandas as pd

def download_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Download historical stock data from Yahoo Finance.
    """
    data = yf.download(ticker, start=start, end=end)
    return data
