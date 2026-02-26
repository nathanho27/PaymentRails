"""
This script will build the financial and performance metrics used in analytics and dashboards.

The goal is to output a small summary table for dashboard callouts:
data/analytics/summary_metrics.csv
"""

import pandas as pd
from pathlib import Path


# The build_summary_metrics function aggregates key statistics by ticker, such as average daily return and average rolling volatility.
def build_summary_metrics(df):
    summary = (
        df.groupby("ticker")
          .agg(
              avg_daily_return=("daily_return", "mean"),
              avg_rolling_volatility=("rolling_30d_volatility", "mean"),
              max_rolling_volatility=("rolling_30d_volatility", "max")
          )
          .reset_index()
    )

    return summary


# The main function loads the analytics dataset, computes summary metrics, and writes the results to a CSV file for use in dashboards.
def main():
    input_path = Path("data/analytics/market_metrics.csv")
    df = pd.read_csv(input_path)

    summary = build_summary_metrics(df)

    output_path = Path("data/analytics/summary_metrics.csv")
    summary.to_csv(output_path, index=False)

    print(f"Summary metrics saved to {output_path}")


# The script can be run directly to generate the summary metrics table.
if __name__ == "__main__":
    main()