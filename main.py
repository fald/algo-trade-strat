# Description:
# This program uses the dual moving average crossover to determine
# buy and sell points of stock.

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
figsize = (12.5, 4.5)

filename = "AAPL.csv"
#filename = "kaggle_AAPL.csv"

aapl = pd.read_csv(filename)

plt.figure(figsize=figsize)
plt.plot(aapl['Adj Close'], label="AAPL")
plt.title("Apple's adjusted closing price history")
#plt.xlabel("29 Sept 2014 - 29 Mar 2018")
plt.ylabel("Adj. close prices - USD")
plt.legend(loc="upper left")
plt.show()

# Simple moving average, 30 day window.
sma30 = pd.DataFrame()
sma30['Adj Close'] = aapl['Adj Close'].rolling(window=30).mean()

# Long term average
sma100 = pd.DataFrame()
sma100['Adj Close'] = aapl['Adj Close'].rolling(window=100).mean()

# Visualise 
plt.figure(figsize=figsize)
plt.plot(aapl['Adj Close'], label="AAPL")
plt.plot(sma30['Adj Close'], label="30-day")
plt.plot(sma100['Adj Close'], label="100-day")
plt.title("Apple's adjusted closing price history")
#plt.xlabel("29 Sept 2014 - 29 Mar 2018")
plt.ylabel("Adj. close prices - USD")
plt.legend(loc="upper left")
plt.show()


# New dataframe
data = pd.DataFrame()
data['AAPL'] = aapl['Adj Close']
data['SMA30'] = sma30['Adj Close']
data['SMA100'] = sma100['Adj Close']


# Return buy/sell prices to plot on chart directly
def buy_sell(data):
    buy = []
    sell = []
    flag = -1 # When do moving averages cross?
    
    for i in range(len(data)):
        if data['SMA30'][i] > data['SMA100'][i]:
            if flag != 1:
                buy.append(data['AAPL'][i])
                sell.append(np.nan)
                flag = 1
            else:
                buy.append(np.nan)
                sell.append(np.nan)
        elif data['SMA30'][i] < data['SMA100'][i]:
            if flag != 0:
                buy.append(np.nan)
                sell.append(data['AAPL'][i])
                flag = 0
            else:
                buy.append(np.nan)
                sell.append(np.nan)
        else:
            buy.append(np.nan)
            sell.append(np.nan)
            
    return buy, sell


b_s = buy_sell(data)
data['Buy Signal Price'] = b_s[0]
data['Sell Signal Price'] = b_s[1]

# Visualise data + strategy
plt.figure(figsize=figsize)
plt.plot(data['AAPL'], label='AAPL', alpha=0.35)
plt.plot(data['SMA30'], label='SMA30', alpha=0.35)
plt.plot(data['SMA100'], label='SMA100', alpha=0.35)
plt.scatter(data.index, data['Buy Signal Price'], label="Buy", marker="^", color="green")
plt.scatter(data.index, data['Sell Signal Price'], label="Sell", marker="v", color="red")
plt.title("Apple Adj Close Price History - Buy/Sell Signals")
plt.ylabel("Adj. close prices - USD")
plt.legend(loc='upper left')
plt.plot()






