"""
This script generates additional market relationship metrics used in the
Market Relationship Analysis dashboard.

The goal is to compute rolling correlations, rolling beta, and relative
performance between Visa, Mastercard, and the S&P 500.

Output:
data/analytics/correlation_metrics.csv
"""

import pandas as pd
from pathlib import Path

# Load the analytics dataset containing daily returns
input_path = Path("data/analytics/market_metrics.csv")
df = pd.read_csv(input_path)

# Pivot returns so each ticker becomes its own column
returns = df.pivot(index="date", columns="ticker", values="daily_return")

# Ensure chronological ordering for rolling calculations
returns = returns.sort_index()

# Rename tickers for cleaner column names
returns = returns.rename(columns={
    "^GSPC": "sp500",
    "V": "visa",
    "MA": "mastercard"
})

# Compute 60-day rolling correlations vs the S&P 500
visa_sp500_correlation = returns["visa"].rolling(60).corr(returns["sp500"])
mastercard_sp500_correlation = returns["mastercard"].rolling(60).corr(returns["sp500"])

# Compute rolling correlation between Visa and Mastercard
visa_mastercard_correlation = returns["visa"].rolling(60).corr(returns["mastercard"])

# Compute rolling covariance for beta calculations
rolling_cov_visa = returns["visa"].rolling(60).cov(returns["sp500"])
rolling_cov_mastercard = returns["mastercard"].rolling(60).cov(returns["sp500"])

# Compute rolling market variance (beta denominator)
rolling_var_market = returns["sp500"].rolling(60).var()

# Calculate rolling beta vs the S&P 500
visa_beta = rolling_cov_visa / rolling_var_market
mastercard_beta = rolling_cov_mastercard / rolling_var_market

# Compute cumulative returns for performance comparison
cumulative_returns = (1 + returns).cumprod()

# Calculate performance relative to the S&P 500
visa_relative_performance = cumulative_returns["visa"] / cumulative_returns["sp500"]
mastercard_relative_performance = cumulative_returns["mastercard"] / cumulative_returns["sp500"]

# Compute performance spread between Visa and Mastercard
visa_vs_mastercard_performance = cumulative_returns["visa"] / cumulative_returns["mastercard"]

# Compute daily return spread vs market
visa_market_spread = returns["visa"] - returns["sp500"]
mastercard_market_spread = returns["mastercard"] - returns["sp500"]

# Market baseline used as reference line in Tableau
market_baseline = 1

# Build the final dataset used in the Tableau dashboard
metrics = pd.DataFrame({
    "date": returns.index,
    "visa_sp500_correlation": visa_sp500_correlation,
    "mastercard_sp500_correlation": mastercard_sp500_correlation,
    "visa_mastercard_correlation": visa_mastercard_correlation,
    "visa_beta": visa_beta,
    "mastercard_beta": mastercard_beta,
    "visa_relative_performance": visa_relative_performance,
    "mastercard_relative_performance": mastercard_relative_performance,
    "visa_vs_mastercard_performance": visa_vs_mastercard_performance,
    "visa_market_spread": visa_market_spread,
    "mastercard_market_spread": mastercard_market_spread,
    "market_baseline": market_baseline
}).reset_index(drop=True)

# Save metrics to the analytics layer for dashboard use
output_path = Path("data/analytics/correlation_metrics.csv")
metrics.to_csv(output_path, index=False)

print(f"Correlation metrics saved to {output_path}")

