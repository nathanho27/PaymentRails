"""
This script loads and standardizes financial fundamentals for Visa and Mastercard.

The goal is to create a structured dataset of yearly financial metrics that can
be used in dashboards alongside market performance data.

Output:
data/raw/financials.csv
"""

"""
This script loads and standardizes financial fundamentals for Visa and Mastercard.

The goal is to create a structured dataset of yearly financial metrics that can
be used in dashboards alongside market performance data.

Output:
data/analytics/financials.csv
"""

import pandas as pd
import yfinance as yf
from pathlib import Path


# The get_financials function pulls annual financial statement data and extracts
# key metrics such as revenue, operating income, and net income.
def get_financials(tickers):
    records = []
    for ticker in tickers:
        t = yf.Ticker(ticker)
        financials = t.financials.T
        for date, row in financials.iterrows():
            revenue = row.get("Total Revenue")
            operating_income = row.get("Operating Income")
            net_income = row.get("Net Income")
            operating_margin = None
            if revenue and operating_income:
                operating_margin = operating_income / revenue
            records.append({
                "ticker": ticker,
                "year": date.year,
                "revenue": revenue,
                "operating_income": operating_income,
                "net_income": net_income,
                "operating_margin": operating_margin
            })

    df = pd.DataFrame(records)
    # Sort values to ensure calculations like growth are applied correctly
    df = df.sort_values(["ticker","year"])
    # Net margin measures how much profit is generated per dollar of revenue
    df["net_margin"] = df["net_income"] / df["revenue"]
    # Revenue growth measures year-over-year company expansion
    df["revenue_growth"] = df.groupby("ticker")["revenue"].pct_change()
    return df

# The main function loads financial data and writes the resulting dataset
# to the analytics folder for use in dashboards.
def main():
    tickers = ["V","MA"]
    df = get_financials(tickers)
    output_dir = Path("data/analytics")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "financials.csv"
    df.to_csv(output_path, index=False)
    print(f"Financial data saved to {output_path}")

# Allows the script to be run directly
if __name__ == "__main__":
    main()