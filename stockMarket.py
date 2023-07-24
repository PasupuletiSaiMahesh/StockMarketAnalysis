import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
stock_symbol = 'AAPL'
start_date = '2022-07-23'
end_date = '2023-07-23'

stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
# Check the first few rows of the data
print(stock_data.head())

# Check for missing values
print(stock_data.isnull().sum())

# Handle missing values (if any)
stock_data = stock_data.dropna()
# Calculate daily returns
stock_data['Daily_Return'] = stock_data['Adj Close'].pct_change()

# Calculate mean and standard deviation of daily returns
mean_daily_return = stock_data['Daily_Return'].mean()
std_daily_return = stock_data['Daily_Return'].std()

print("Mean Daily Return:", mean_daily_return)
print("Standard Deviation of Daily Return:", std_daily_return)
# Plot daily closing prices
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Adj Close'])
plt.title('Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid()
plt.show()
