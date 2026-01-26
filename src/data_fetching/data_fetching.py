import yfinance as yf
import pandas as pd
import numpy as np
import time
# -----------------------------
# 1. CONFIG
# -----------------------------
stocks = [
    "AAPL",   # Technology
    "MSFT",   # Technology
    "JPM",    # Banking
    "XOM",    # Energy
    "JNJ",    # Healthcare
    "PG",     # Consumer Goods
    "AMZN",   # Retail
    "TSLA",   # Automotive
    "NVDA",   # Semiconductor
    "VZ"      # Telecom
    "META",   # Social Media / Tech
    "GOOGL",  # Internet / AI
    "NFLX",   # Media / Streaming
    "INTC",   # Semiconductors
    "DIS"    # Entertainment
]


market_index = "^GSPC"  # S&P 500
tickers = stocks + [market_index]
start_date = "2019-01-01"
end_date = "2024-01-01"

# -----------------------------
# Download Data
# -----------------------------
print("Downloading data...")
data = yf.download(
    tickers,
    start=start_date,
    end=end_date,
    group_by="ticker",
    auto_adjust=True,
    threads=True
)

# -----------------------------
# Convert to CLEAN LONG FORMAT
# -----------------------------
records = []

for ticker in tickers:
    if ticker not in data.columns.levels[0]:
        print(f"Skipping {ticker} (no data)")
        continue

    df = data[ticker].reset_index()

    df["Ticker"] = ticker
    df = df[["Date", "Ticker", "Close", "Volume"]]
    df.rename(columns={"Close": "Adj Close"}, inplace=True)

    records.append(df)

portfolio_df = pd.concat(records, ignore_index=True)

# -----------------------------
# Final Checks
# -----------------------------
print("\nFinal dataframe shape:", portfolio_df.shape)
print("\nColumns:", portfolio_df.columns)
print("\nSample rows:")
print(portfolio_df.head())

# # -----------------------------
# # 7. SAVE TO CSV
# # -----------------------------

portfolio_df.to_csv(
    r"C:\Users\mohamedirfan\OneDrive\Desktop\internship\zaalima\project_2[financial_analytics]\week_1\data\clean_portfolio_data.csv",
    index=False
)

print("\n✅ FINAL_CLEAN_PORTFOLIO.csv saved successfully")
