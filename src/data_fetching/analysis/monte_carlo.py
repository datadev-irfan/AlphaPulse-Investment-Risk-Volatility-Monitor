import pandas as pd
import numpy as np

# Load log return data
df = pd.read_csv("data/processed/log_returns_data.csv")

# Calculate portfolio daily mean return and volatility
mean_return = df["Log_Return"].mean()
volatility = df["Log_Return"].std()

# Simulation parameters
initial_value = 100000  # ₹1,00,000
trading_days = 252
num_simulations = 10000

# Generate random daily returns
np.random.seed(42)  # reproducibility
daily_returns = np.random.normal(
    mean_return,
    volatility,
    (trading_days, num_simulations)
)

# Simulate portfolio paths
portfolio_paths = initial_value * np.exp(
    np.cumsum(daily_returns, axis=0)
)

# Final portfolio values after 1 year
final_values = portfolio_paths[-1]

print("Monte Carlo simulation completed")
print("Sample final values:", final_values[:5])

# NOTE:
# Monte Carlo results are generated dynamically and not stored,
# as simulations are stochastic and reproducible from inputs.