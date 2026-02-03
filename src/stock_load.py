"""
This script loads market data for payment networks (Visa, Mastercard).

The goal is to output raw market price data to data/raw/.
Output: data/raw/market_prices.csv
"""

import pandas as pd
import yfinance as yf
from pathlib import Path


def get_market_prices(tickers, start_date="2010-01-01"):
    raw = yf.download(tickers, start=start_date, progress=False, threads=False, auto_adjust=True)

    prices = raw["Close"]
    prices = (prices.reset_index()
                     .melt(id_vars="Date", var_name="ticker", value_name="adj_close")
                     .rename(columns={"Date": "date"})
                     .dropna())

    return prices


def main():
    tickers = ["V", "MA"]
    df = get_market_prices(tickers)

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "market_prices.csv"
    df.to_csv(output_path, index=False)

    print(f"Market price data saved to {output_path}")


if __name__ == "__main__":
    main()