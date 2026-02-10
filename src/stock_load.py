"""
This script loads market data for payment networks (Visa, Mastercard) and the overall market index (S&P 500).

The goal is to output raw market price data to data/raw/.
Output: data/raw/market_prices.csv
"""
...
def main():
    tickers = ["V", "MA", "^GSPC"]  # Visa, Mastercard, S&P 500
    df = get_market_prices(tickers)

import pandas as pd
import yfinance as yf
from pathlib import Path

# The get_market_prices function takes a list of stock tickers and an optional start date, downloads the historical market data for those tickers using the yfinance library, and processes the data to return a tidy DataFrame with the date, ticker, and adjusted closing price. The data is then saved to a CSV file in the specified output directory.
def get_market_prices(tickers, start_date="2010-01-01"): # Default start date for historical data
    raw = yf.download(tickers, start=start_date, progress=False, threads=False, auto_adjust=True) # Download historical market data for the specified tickers

    prices = raw["Close"] # Extract the closing prices from the downloaded data
    prices = (prices.reset_index()
                     .melt(id_vars="Date", var_name="ticker", value_name="adj_close")
                     .rename(columns={"Date": "date"})
                     .dropna()) # The resulting DataFrame has three columns: 'date', 'ticker', and 'adj_close', where 'date' is the date of the price, 'ticker' is the stock ticker (e.g., V, MA, GSPC), and 'adj_close' is the adjusted closing price for that date and ticker. The dropna() function is used to remove any rows with missing values.
    return prices

# The main function defines a list of stock tickers (Visa, Mastercard, and S&P 500), calls the get_market_prices function to retrieve the market price data for those tickers, and then saves the resulting DataFrame to a CSV file in the data/raw/ directory. The output file is named market_prices.csv.
def main():
    tickers = ["V", "MA", "^GSPC"] # Visa, Mastercard, S&P 500
    df = get_market_prices(tickers)

    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "market_prices.csv"
    df.to_csv(output_path, index=False)

    print(f"Market price data saved to {output_path}")

# The script can be run directly, and it will execute the main function to perform the data loading and saving process.
if __name__ == "__main__":
    main()