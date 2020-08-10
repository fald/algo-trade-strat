# Description:
# This program uses the dual moving average crossover to determine
# buy and sell points of stock.

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
figsize = (12.5, 4.5)
plt.figure(figsize=figsize)

filename = "AAPL.csv"

aapl = pd.read_csv(filename)

plt.plot(aapl['Adj Close'], label="AAPL")
plt.title("Apple's adjusted closing price history")
plt.xlabel("29 Sept 2014 - 29 Mar 2018")
plt.ylabel("Adj. close prices - USD")
plt.legend(loc="upper left")
plt.show()

