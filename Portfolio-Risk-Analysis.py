#!/usr/bin/env python
# coding: utf-8

# Historical VaR:

# In[ ]:


import yfinance as yf
import pandas as pd

tickers = ["AAPL", "MSFT", "TSLA"]

data = yf.download(tickers, start="2022-01-01", end="2024-01-01")['Close']

returns = data.pct_change().dropna()

weight = [1/3, 1/3, 1/3]

protfolio_return = returns.dot(weight)

VaR_95 = protfolio_return.quantile(0.05)  #Historical VaR:list all data and find the data corrsponding in 5% position

print("VaR (95%):", VaR_95)



import matplotlib.pyplot as plt

plt.hist(protfolio_return, bins=50)
plt.axvline(VaR_95, color='r', linestyle='dashed', linewidth=2)
plt.title("Protfolio Returns Distribution with VaR")
plt.savefig("historical_var.png")
plt.show()


# Monte karlo simulation of profolio returns
# 

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

mu = protfolio_return.mean()
sigma = protfolio_return.std()
n_simulation = 10000

simulated_returns = np.random.normal(mu,sigma,n_simulation)

VaR_95 = np.percentile(simulated_returns,5)
print("Monte Carlo VaR(95%)",VaR_95)

plt.figure(figsize=(10,5))
plt.hist(simulated_returns, bins=50)
plt.axvline(VaR_95, linestyle='dashed', color='r')
plt.title("Monte Carlo Simulation of Portfolio Returns")
plt.xlabel("Simulated Returns")
plt.ylabel("Frequency")
plt.savefig("monte_carlo.png")
plt.show()


# Backtesting: if the abnormal cases which means that the real return is larger than VaR_95 are less than 5%.
# if 1-500days,VaR_95=-3%, and in the 501st day,VaR_95= -2%, then normal.

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

window = 100
VaR_list = []
Actual_list = []

for i in range(window, len(protfolio_return)):
    past_data = protfolio_return[i-window:i]
    
    mu = past_data.mean()
    sigma = past_data.std()
    n_simulation = 10000
    simulated_returns = np.random.normal(mu,sigma,n_simulation)

    VaR = np.percentile(simulated_returns,5)

    VaR_list.append(VaR)
    Actual_list.append(protfolio_return[i])

VaR_array = np.array(VaR_list)
Actual_array = np.array(Actual_list)
    
exceptions = Actual_array < VaR_array 
n_exceptions = exceptions.sum()
n_total = len(Actual_array)
exception_rate = n_exceptions / n_total

print("Exception_rate: ",exception_rate)
    

plt.figure(figsize=(10,5))

plt.plot(Actual_array, label="Actual Return")
plt.plot(VaR_array, label="VaR(95%)",color="red")

plt.scatter(np.where(exceptions),Actual_array[exceptions],label='Exceptions',color='black')

plt.legend()
plt.title("VaR Backtesting")
plt.savefig("backtesting.png")
plt.show()
    


# In[ ]:




