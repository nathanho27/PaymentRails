"""
This script generates market regime metrics used in the
Market Regime Analysis dashboard.

The goal is to classify market environments based on
S&P 500 volatility and analyze how Visa and Mastercard
behave during different market conditions.

Output:
data/analytics/regime_metrics.csv
"""

import pandas as pd
from pathlib import Path


# Load analytics dataset containing daily returns and volatility metrics
input_path = Path("data/analytics/market_metrics.csv")
df = pd.read_csv(input_path)


# Extract S&P 500 volatility to define market regimes
market_vol = (
    df[df["ticker"] == "^GSPC"][["date", "rolling_30d_volatility"]]
    .rename(columns={"rolling_30d_volatility": "sp500_volatility"})
)


# Merge S&P 500 volatility back into the full dataset
df = df.merge(market_vol, on="date", how="left")


# Classify market volatility regimes based on S&P 500 volatility
def classify_regime(vol):

    if pd.isna(vol):
        return None
    elif vol < 0.15:
        return "Low Volatility"
    elif vol < 0.25:
        return "Moderate Volatility"
    else:
        return "High Volatility"

df["market_regime"] = df["sp500_volatility"].apply(classify_regime)


# Extract S&P 500 daily returns to compute performance relative to the market
sp500_returns = (
    df[df["ticker"] == "^GSPC"][["date", "daily_return"]]
    .rename(columns={"daily_return": "sp500_return"})
)

df = df.merge(sp500_returns, on="date", how="left")


# Compute return spread vs the market
df["return_spread_vs_market"] = df["daily_return"] - df["sp500_return"]


# Compute simple risk-adjusted return
df["risk_adjusted_return"] = df["daily_return"] / df["rolling_30d_volatility"]
df.loc[df["rolling_30d_volatility"] == 0, "risk_adjusted_return"] = None


# Keep only columns needed for the dashboard dataset
regime_metrics = df[
    [
        "date",
        "ticker",
        "daily_return",
        "rolling_30d_volatility",
        "sp500_volatility",
        "market_regime",
        "return_spread_vs_market",
        "risk_adjusted_return",
    ]
]


# Save dataset for Tableau dashboard
output_path = Path("data/analytics/regime_metrics.csv")
regime_metrics.to_csv(output_path, index=False)

print(f"Market regime metrics saved to {output_path}")