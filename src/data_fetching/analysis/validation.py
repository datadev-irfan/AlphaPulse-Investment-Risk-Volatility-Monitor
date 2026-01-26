import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis

# Load historical log returns
df = pd.read_csv("data/processed/log_returns_data.csv")

historical_returns = df["Log_Return"]

# Monte Carlo parameters (same as before)
mean_return = historical_returns.mean()
volatility = historical_returns.std()
trading_days = 252
num_simulations = 10000

np.random.seed(42)

# Simulate returns (not prices)
simulated_returns = np.random.normal(
    mean_return,
    volatility,
    trading_days * num_simulations
)

# Calculate statistics
hist_skew = skew(historical_returns)
hist_kurt = kurtosis(historical_returns, fisher=False)

sim_skew = skew(simulated_returns)
sim_kurt = kurtosis(simulated_returns, fisher=False)

print("Historical Returns:")
print("Skewness:", hist_skew)
print("Kurtosis:", hist_kurt)

print("\nSimulated Returns:")
print("Skewness:", sim_skew)
print("Kurtosis:", sim_kurt)
