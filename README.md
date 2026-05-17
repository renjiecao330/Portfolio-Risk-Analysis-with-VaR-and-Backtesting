# Portfolio Risk Analysis with VaR and Backtesting

## Overview

This project analyzes the risk of a portfolio composed of:

- AAPL
- MSFT
- TSLA

using:

- Historical VaR
- Monte Carlo Simulation
- VaR Backtesting

The objective is to estimate potential portfolio losses and evaluate model performance over time.

---

## Methods

### Historical VaR
- Calculated daily portfolio returns
- Estimated 95% VaR using historical return distribution

### Monte Carlo VaR
- Simulated 10,000 portfolio return scenarios
- Assumed normally distributed returns

### VaR Backtesting
- Implemented rolling 100-day VaR estimation
- Compared predicted VaR with actual returns
- Calculated exception rate

---

## Results

The model successfully:

- Estimated portfolio downside risk
- Identified VaR exceptions
- Visualized changing market risk over time

The observed exception rate was close to the theoretical 5% level.

---

## Tools

- Python
- pandas
- numpy
- matplotlib
- yfinance

---

## Key Skills Demonstrated

- Financial data analysis
- Risk modeling
- Monte Carlo simulation
- Backtesting
- Data visualization

---

## Future Improvements

Possible improvements include:

- GARCH volatility modeling
- Fat-tail distributions
- Expected Shortfall (CVaR)
