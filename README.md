# AlphaPulse – Investment Risk & Volatility Monitor

## Week 1: Data Acquisition & Cleaning

### Objective
Collect and clean historical market data for a diversified stock portfolio to enable downstream risk analytics.

### Data
- 15 US stocks across multiple sectors
- S&P 500 as market benchmark
- Time Period: 2019–2024

### Output
- Clean, adjusted price dataset
- Long-format schema suitable for analytics

### Status
Week 1 completed ✔

## 📊 Week 2 – Quantitative Analysis

### Objectives
- Calculate daily log returns using NumPy
- Forecast portfolio value using Monte Carlo Simulation (10,000 runs)
- Validate simulated return distribution against historical market behavior

### Key Implementations
- **Log Returns**: Computed using vectorized NumPy operations for efficiency
- **Monte Carlo Simulation**:
  - 10,000 simulations
  - 252 trading days (1 year horizon)
  - Based on historical mean and volatility
- **Statistical Validation**:
  - Skewness comparison
  - Kurtosis (tail risk) analysis

### Results Summary
- Historical returns show negative skewness and high kurtosis (fat tails)
- Simulated returns approximate a normal distribution
- Confirms correct implementation and highlights real-market risk behavior

### Status
Week 2 completed ✔

