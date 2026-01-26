import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv("data/processed/clean_portfolio_data.csv")

# Ensure Date is datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort properly (VERY IMPORTANT)
df = df.sort_values(by=["Ticker", "Date"])

# Calculate daily log returns per stock
df["Log_Return"] = df.groupby("Ticker")["Adj Close"].transform(
    lambda x: np.log(x / x.shift(1))
)

# Drop first row of each stock (NaN log return)
df = df.dropna(subset=["Log_Return"])

# Save output for next steps
df.to_csv("data/processed/log_returns_data.csv", index=False)

print("Daily log returns calculated successfully")
print(df.head())
