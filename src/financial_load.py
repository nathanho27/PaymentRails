"""
This script loads and standardizes financial fundamentals for Visa and Mastercard.

The goal is to output raw financial metrics (e.g., revenue, margins) to:
data/raw/financials.csv

This will later be used to enrich market performance analysis with
business context.
"""

import pandas as pd
from pathlib import Path


# The get_financials function is a placeholder for loading financial data from public sources (e.g., financial statements, APIs).
def get_financials(tickers):
    # Placeholder implementation
    data = {
        "ticker": tickers,
        "revenue": [None for _ in tickers],
        "operating_margin": [None for _ in tickers]
    }

    return pd.DataFrame(data)


# The main function defines the tickers to load fundamentals for and writes the resulting dataset to disk.
def main():
    tickers = ["V", "MA"]
    df = get_financials(tickers)

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "financials.csv"
    df.to_csv(output_path, index=False)

    print(f"Financial data saved to {output_path}")


# The script can be run directly to generate the raw financials dataset.
if __name__ == "__main__":
    main()