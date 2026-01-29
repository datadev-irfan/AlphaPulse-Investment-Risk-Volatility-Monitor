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

## Week 3: Visual Storytelling & Scenario Analysis (Tableau)

### Objective
Transform quantitative risk metrics into an interactive visual dashboard that allows users to perform real-time
“What-If” scenario analysis on the investment portfolio.

### Key Features
- Connected Tableau directly to cleaned portfolio CSV data
- Built dynamic What-If parameters to simulate market shocks
- Interactive comparison of portfolio volatility before and after shock
- KPI cards for:
  - Value at Risk (VaR %)
  - Expected Return (%)
  - Portfolio Volatility
- All visuals update instantly when scenario parameters change

### Dashboard Highlights
- Portfolio Value Over Time (Line Chart)
- Volatility Before vs After Shock (Bar Chart)
- Scenario Control: Tech Sector Shock (%)
- Risk KPIs for quick executive insights

### Outcome
This dashboard enables business users to explore downside risk, stress scenarios,
and portfolio behavior without writing code, bridging quantitative finance and decision-making.
