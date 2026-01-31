# AlphaPulse – Investment Risk & Volatility Monitor

## 📊 Week 1: Data Acquisition & Cleaning

### Objective
Collect and clean historical market data for a diversified stock portfolio to enable downstream risk analytics.

### Data
- 15 US stocks across multiple sectors
- S&P 500 as market benchmark
- Time Period: 2019–2024

### Output
- Clean, adjusted price dataset
- Long-format schema suitable for analytics


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


## 📊 Week 3: Visual Storytelling & Scenario Analysis (Tableau)

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

## Week 4 – Finalization (AlphaPulse)
### Objective

Week 4 focused on finalizing the AlphaPulse project by implementing automation, executive-level reporting, and financial validation. The goal was to make the system production-ready and decision-maker friendly.

### Key Features
- Automated Market Data Refresh
- Executive Summary Dashboard
-  Financial Accuracy Validation


### Outcome
By the end of Week 4:
-AlphaPulse became production-ready
-Risk metrics were verified
-Executive reporting was implemented
-Data refresh process was streamlined

### 🚀 Conclusion

Week 4 completed the AlphaPulse system by ensuring accuracy, usability, and professional presentation. The project now functions as a realistic portfolio risk monitoring solution.